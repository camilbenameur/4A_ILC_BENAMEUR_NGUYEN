import os
import json
from flask import Flask, request, jsonify
import redis
from datetime import datetime
from flask_bcrypt import Bcrypt
from flask_cors import CORS


def create_app(test_config=None):
    app = Flask(__name__, instance_relative_config=True)
    CORS(app)
    app.config.from_mapping(
        SECRET_KEY='dev',
        DEBUG=True,
    )

    if test_config is None:
        app.config.from_pyfile('config.py', silent=True)
    else:
        app.config.from_mapping(test_config)

    try:
        os.makedirs(app.instance_path)
    except OSError:
        pass
        
    redis_db = redis.StrictRedis(host='my_redis', port=6379, db=0, decode_responses=True)
    bcrypt = Bcrypt(app)
    
    @app.route('/', methods=['GET'])
    def hello():
        return 'Hello, Flask!'
    
    @app.route('/register', methods=['POST'])
    def register():
        try:
            data = request.json
            email = data.get('email')
            password = data.get('password')

            if not email or not password:
                return jsonify({'error': 'Email and password are required'}), 400

            hashed_password = bcrypt.generate_password_hash(password)

            redis_key = f'user:{email}'
            redis_db.hset(redis_key, 'email', email)
            redis_db.hset(redis_key, 'password', hashed_password)

            return jsonify({'message': 'User registered successfully'})

        except Exception as e:
            return jsonify({'error': str(e)}), 500
        
    @app.route('/signin', methods=['POST'])
    def signin():
        try:
            data = request.json
            email = data.get('email')
            password = data.get('password')

            if not email or not password:
                return jsonify({'error': 'Email and password are required'}), 400

            redis_key = f'user:{email}'
            stored_password = redis_db.hget(redis_key, 'password')

            if stored_password and bcrypt.check_password_hash(stored_password, password):
                return jsonify({'message': 'User signed in successfully'})
            else:
                return jsonify({'error': 'Invalid email or password'}), 401

        except Exception as e:
            return jsonify({'error': str(e)}), 500
    
    @app.route('/tweet', methods=['POST'])
    def tweet():
        data = request.json
        username = data.get('username')
        message = data.get('tweet')
        if username and message:
            tweet = {
                'author': username,
                'tweet': message
            }
            timestamp = datetime.now().strftime("%Y%m%d%H%M%S")
            redis_db.set(timestamp, json.dumps(tweet))
            
            user_key = f"user:{username}"
            redis_db.sadd(user_key, timestamp)
            
            for word in message.split():
                if word.startswith('#'):
                    topic_key = f"topic:{word}"
                    redis_db.sadd(topic_key, timestamp)

            return jsonify({'message': 'Tweeted successfully.'}), 201
        else:
            return jsonify({'error': 'Missing username or tweet content.'}), 400
        
    @app.route('/tweets', methods=['GET'])
    def display_tweets():
        return jsonify(redis_db.keys())

    @app.route('/user_tweets/<username>', methods=['GET'])
    def user_tweets(username):
        user_key = f"user:{username}"
        tweet_keys = redis_db.smembers(user_key)
        tweets = [json.loads(redis_db.get(key)) for key in tweet_keys]
        return jsonify(tweets)
        
    @app.route('/topics', methods=['GET'])
    def display_topics():
        topic_keys = redis_db.keys("topic:*")
        topics = [topic_key.split(":")[1] for topic_key in topic_keys]
        return jsonify(topics)            

    @app.route('/topic_tweets/<topic>', methods=['GET'])
    def topic_tweets(topic):
        topic_key = f"topic:{topic}"
        tweet_keys = redis_db.smembers(topic_key)
        tweets = [json.loads(redis_db.get(key)) for key in tweet_keys]
        return jsonify(tweets)

    return app
