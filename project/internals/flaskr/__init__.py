import os
import json
from flask import Flask, request, jsonify
import redis
from datetime import datetime

def create_app(test_config=None):
    app = Flask(__name__, instance_relative_config=True)
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

    redis_db = redis.StrictRedis(host='localhost', port=6379, db=0, decode_responses=True)

    @app.route('/', methods=['GET'])
    def hello():
        return 'Hello, Flask!'
    
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
