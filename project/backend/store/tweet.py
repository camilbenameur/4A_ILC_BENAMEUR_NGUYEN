from redis import Redis
from flask import jsonify
import uuid
import json
from datetime import datetime


class Tweet:
    user: str
    message: str

    def __init__(self, user: str, message: str):
        self.user = user
        self.message = message


class TweetStore:
    db: Redis

    def __init__(self, db: Redis):
        self.db = db

    def tweet_key(self, timestamp: str) -> str:
        return f"tweet:{timestamp}"

    def user_key(self, email: str) -> str:
        return f"user:{email}"

    def topic_key(self, topic: str) -> str:
        return f"topic:{topic}"

    def create_tweet(self, email: str, message: str) -> Tweet:
        tweet = Tweet(email, message)
        timestamp = datetime.now().strftime("%Y%m%d%H%M%S")
        self.db.set(self.tweet_key(timestamp), json.dumps(tweet.__dict__))
        self.db.sadd(self.user_key(email), timestamp)
        for word in message.split():
            if word.startswith("#"):
                word = word[1:]
                self.db.sadd(self.topic_key(word), timestamp)
        return tweet

    def get_tweets(self) -> list:
        all_keys = self.db.keys()
        tweets = []
        for key in all_keys:
            if not key.startswith("user:") and not key.startswith("topic:"):
                timestamp = key
                tweet_json = self.db.get(timestamp)
                tweet = json.loads(tweet_json)
                tweet["timestamp"] = timestamp
                tweets.append(tweet)
        return tweets

    def get_user_tweets(self, email: str) -> list:
        user_tweets = self.db.keys(
            pattern = f"user:{email}"
            )        
        return user_tweets

    def get_topic_tweets(self, topic: str) -> list:
        topic_keys = self.db.smembers(self.topic_key(topic))
        topic_tweets = []
        for key in topic_keys:
            tweet_json = self.db.get(self.tweet_key(key))
            tweet = json.loads(tweet_json)
            tweet["timestamp"] = self.tweet_key(key)
            topic_tweets.append(tweet)
        return topic_tweets

    def get_topics(self) -> list:
        topic_keys = self.db.keys("topic:*")
        topics = [topic_key.split(":")[1] for topic_key in topic_keys]
        return topics