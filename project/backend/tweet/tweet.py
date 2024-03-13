from flask import Blueprint, request, jsonify, session
from flask_bcrypt import Bcrypt

from redis_db import redis_db
from store.tweet import TweetStore
import json
from datetime import datetime

tweet = Blueprint("tweet", __name__, url_prefix="/tweets")
bcrypt = Bcrypt()
tweet_store = TweetStore(redis_db)


@tweet.route("", methods=["POST"])
def create_tweet():
    data = request.json
    email = data.get("email")
    message = data.get("tweet")

    if email and message:
        tweet = tweet_store.create_tweet(email, message)
        return jsonify(tweet.__dict__), 201
    else:
        return jsonify({"error": "Missing email or tweet content."}), 400


@tweet.route("", methods=["GET"])
def get_tweets():
    user = request.args.get("user")
    if user:
        tweets = tweet_store.get_user_tweets(user)
        return jsonify(tweets), 200

    topic = request.args.get("topic")
    if topic:
        tweets = tweet_store.get_topic_tweets(topic)
        return jsonify(tweets), 200
    return jsonify(tweet_store.get_tweets()), 200


@tweet.route("/get_user", methods=["GET"])
def get_user():
    return jsonify({"user": session.get("user")}), 200


@tweet.route('/retweet', methods=['POST'])
def retweet():
    data = request.json
    email = data.get('email')
    timestamp = data.get('timestamp')
    post_email = data.get('email_post')

    if email and timestamp and post_email:
        tweet_json = redis_db.get(timestamp)
        if tweet_json:
            
            retweet_timestamp = datetime.now().strftime("%Y%m%d%H%M%S")
            retweet_key = f"retweet:{retweet_timestamp}:{email}"
            tweet = json.loads(tweet_json)
            retweet = {
                'timestamp' : timestamp,
                'user': email,
                'message': tweet['message'],
                'post_email' : post_email
            }
            redis_db.set(retweet_key, json.dumps(retweet))
            
            return jsonify({'message': 'Retweet successful', 'retweeted_tweet': retweet}), 201
        else:
            return jsonify({'error': 'Tweet not found'}), 404
    else:
        return jsonify({'error': 'Missing email or timestamp'}), 400