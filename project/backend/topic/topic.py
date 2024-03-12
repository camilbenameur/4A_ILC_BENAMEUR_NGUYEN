from flask import Blueprint, request, jsonify, session
from flask_bcrypt import Bcrypt

from redis_db import redis_db
from store.topic import TopicStore, Topic

topic = Blueprint("topic", __name__, url_prefix="/topic")
bcrypt = Bcrypt()
topic_store = TopicStore(redis_db)
    

@topic.route("/get_topics", methods=["GET"])
def get_topics():
    return jsonify(topic_store.get_topics()), 200