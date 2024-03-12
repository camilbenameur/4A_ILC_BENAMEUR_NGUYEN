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
        keys = self.db.keys(pattern='topic:*')
        topics = [key.replace('topic:', '') for key in keys]
        return topics
    
    def get_topic(self, name: str) -> Topic:
        topic_json = self.db.get(self.topic_key(name))
        topic = json.loads(topic_json)
        return topic
    
    def get_keys(self) -> list:
        return self.db.keys()
    