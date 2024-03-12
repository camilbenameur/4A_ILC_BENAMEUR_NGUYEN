from redis import Redis
import json


class Topic:
    name: str

    def __init__(self, name: str):
        self.name = name
        
class TopicStore:
    db: Redis

    def __init__(self, db: Redis):
        self.db = db

    def topic_key(self, name: str) -> str:
        return f"topic:{name}"
    
    def get_topics(self) -> list:
        all_keys = self.db.keys()
        topics = []
        for key in all_keys:
            if key.startswith("#"):
                topic_json = self.db.get(key)
                topic = json.loads(topic_json)
                topics.append(topic)
        return topics
    
    def get_topic(self, name: str) -> Topic:
        topic_json = self.db.get(self.topic_key(name))
        topic = json.loads(topic_json)
        return topic
    