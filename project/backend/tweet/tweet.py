from flask import Blueprint, request, jsonify, session
from flask_bcrypt import Bcrypt

from redis_db import redis_db
from store.tweet import TweetStore, Tweet

tweet = Blueprint("tweet", __name__, url_prefix="/tweet")
bcrypt = Bcrypt()
tweet_store = TweetStore(redis_db)


@tweet.route("/post", methods=["POST"])
def create_tweet():
    data = request.json
    email = data.get("email")
    message = data.get("message")
    
    if email and message:
        tweet = tweet_store.create_tweet(email, message)
        return jsonify(tweet.__dict__), 201
    else:
        return jsonify({"error": "Missing email or tweet content."}), 400


@tweet.route("/get", methods=["GET"])
def get_tweets_json():
    return jsonify(tweet_store.get_tweets()), 200


@tweet.route("/get_user_tweets/<email>", methods=["GET"])
def get_user_tweets(email: str):
    if email:
        return jsonify(tweet_store.get_user_tweets(email)), 200
    else:
        return jsonify({"error": "Missing email"}), 400


@tweet.route("/get_topic_tweets", methods=["GET"])
def get_topic_tweets():
    topic = request.args.get("topic")
    if topic:
        return jsonify(tweet_store.get_topic_tweets(topic)), 200
    else:
        return jsonify({"error": "Missing topic"}), 400


@tweet.route("/get_tweets", methods=["GET"])
def get_tweets():
    return jsonify(tweet_store.get_tweets()), 200


@tweet.route("/get_user", methods=["GET"])
def get_user():
    return jsonify({"user": session.get("user")}), 200

