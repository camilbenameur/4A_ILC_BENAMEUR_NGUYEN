from flask_cors import CORS
from flask import Flask
import os

from auth import auth
from tweet import tweet
from topic import topic


"""
user:{username} -> Hmap(password)
user_tweet:{username} -> Set(tweet_id)
tweet:{tweet_id} -> Hmap(author, tweet)
topic:{topic} -> Set(tweet_id)

"""


def create_app(test_config=None):
    app = Flask(__name__, instance_relative_config=True)
    CORS(app)
    app.config.from_mapping(
        SECRET_KEY="dev",
        DEBUG=True,
    )

    if test_config is None:
        app.config.from_pyfile("config.py", silent=True)
    else:
        app.config.from_mapping(test_config)

    app.register_blueprint(auth.auth)
    app.register_blueprint(tweet.tweet)
    app.register_blueprint(topic.topic)

    return app
