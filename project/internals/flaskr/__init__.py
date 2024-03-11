import os
import json
from flask import Flask, request, jsonify, session
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
                session["email"] = email
                return jsonify({'message': 'User signed in successfully', 'email': session.get("email")})  # Include email in response
            else:
                return jsonify({'error': 'Invalid email or password'}), 401

        except Exception as e:
            return jsonify({'error': str(e)}), 500

        
        
    @app.route('/logout', methods=['GET'])
    def logout():
        session.clear()
        return jsonify({'message': 'Logged out successfully'}), 200
    
    
    @app.route('/tweet', methods=['POST'])
    def tweet():
        data = request.json
        email = data.get('email')
        message = data.get('tweet')
        if email and message:
            tweet = {
                'user': email,
                'message': message
            }
            timestamp = datetime.now().strftime("%Y%m%d%H%M%S")
            redis_db.set(timestamp, json.dumps(tweet))

            for word in message.split():
                if word.startswith('#'):
                    word = word[1:]
                    topic_key = f"topic:{word}"
                    redis_db.sadd(topic_key, timestamp)
            
            user_key = email
            redis_db.sadd(user_key, timestamp)
            
            

            return jsonify({'message': 'Tweeted successfully.'}), 201
        else:
            return jsonify({'error': 'Missing email or tweet content.'}), 400
        
    @app.route('/tweets', methods=['GET'])
    def display_tweets():
        all_keys = redis_db.keys()
        tweets = []

        for key in all_keys:
            # Check if the key consists only of numeric characters
            if key.isdigit():
                tweet_json = json.loads(redis_db.get(key))
                tweet = {
                    'timestamp': key,
                    'user': tweet_json['user'],
                    'message': tweet_json['message']
                }
                tweets.append(tweet)

        return jsonify(tweets)


    @app.route('/user_tweets/<email>', methods=['GET'])
    def user_tweets(email):
        user_key = email
        tweet_keys = redis_db.smembers(user_key)
        tweets = []
        for key in tweet_keys:
            tweet = json.loads(redis_db.get(key))
            tweet['timestamp'] = key
            tweets.append(tweet)
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
        tweets = []
        for key in tweet_keys:
            tweet = json.loads(redis_db.get(key))
            tweet['timestamp'] = key
            tweets.append(tweet)
        return jsonify(tweets)
    
    
    @app.route('/some_route', methods=['GET'])
    def some_route():
        return redis_db.keys()

    return app
