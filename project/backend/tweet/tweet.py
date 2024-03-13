from flask import Blueprint, request, jsonify, session
from flask_bcrypt import Bcrypt

from redis_db import redis_db
from store.tweet import TweetStore

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
