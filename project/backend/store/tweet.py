from redis import Redis
from flask import jsonify
import uuid
import json
from datetime import datetime

from store.user import UserStore


class Tweet:
    user: str
    message: str
    timestamp: str
    id: str

    def __init__(self, user: str, message: str, id: str = None, timestamp: str = None):
        if not id:
            self.id = str(uuid.uuid4())
        if not timestamp:
            self.timestamp = datetime.now().__str__()

        self.user = user
        self.message = message


class TweetStore:
    db: Redis

    def __init__(self, db: Redis):
        self.db = db
        self.user_store = UserStore(db)

    def tweet_key(self, id: str) -> str:
        return f"tweet:{id}"

    def user_key(self, email: str) -> str:
        return email

    def topic_key(self, topic: str) -> str:
        return f"topic:{topic}"

    def create_tweet(self, email: str, message: str) -> Tweet:
        tweet = Tweet(email, message)
        self.db.set(self.tweet_key(tweet.id), json.dumps(tweet.__dict__))
        self.db.sadd(self.user_key(email), tweet.id)
        for word in message.split():
            if word.startswith("#"):
                word = word[1:]
                self.db.sadd(self.topic_key(word), tweet.id)
        return tweet

    def get_tweets(self) -> list:
        all_keys = self.db.keys(pattern="tweet:*")
        return self.get_multiple_tweets(all_keys)

    def get_multiple_tweets(self, tweet_ids: list) -> list:
        tweets = []
        for tweet_id in tweet_ids:
            tweet_json = self.db.get(self.tweet_key(tweet_id))
            tweet = json.loads(tweet_json)
            tweet["id"] = self.tweet_key(tweet_id)
            tweets.append(tweet)
        return sorted(tweets, key=lambda tweet: tweet["timestamp"], reverse=True)

    def get_user_tweets(self, email: str) -> list:
        user_key = email
        tweet_keys = self.db.smembers(user_key)
        return self.get_multiple_tweets(tweet_keys)

    def get_topic_tweets(self, topic: str) -> list:
        topic_keys = self.db.smembers(self.topic_key(topic))
        return self.get_multiple_tweets(topic_keys)

    def get_topics(self) -> list:
        topic_keys = self.db.keys("topic:*")
        topics = [topic_key.split(":")[1] for topic_key in topic_keys]
        return topics
