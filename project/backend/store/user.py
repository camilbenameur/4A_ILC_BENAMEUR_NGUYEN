from redis import Redis
import uuid
import json


class User:
    id: str
    username: str
    email: str
    password: str

    def __init__(self, id: str, username: str, email: str, password: str):
        self.username = username
        self.email = email
        self.password = password
        self.id = id


def user_from_dict(data: dict) -> User:
    return User(data["id"], data["username"], data["email"], data["password"])


class UserStore:
    db: Redis

    def user_email_key(self, email: str) -> str:
        return f"user:email:{email}"

    def user_username_key(self, username: str) -> str:
        return f"user:username:{username}"

    def get_user_key(self, id: str) -> str:
        return f"user:{id}"

    def __init__(self, db: Redis):
        self.db = db

    def create_user(self, username: str, email: str, password: str) -> User:
        id = str(uuid.uuid4())
        user = User(id, username, email, password)
        self.db.set(self.get_user_key(id), json.dumps(user.__dict__))
        self.db.set(self.user_email_key(email), id)
        self.db.set(self.user_username_key(username), id)
        return user

    def email_exists(self, email: str) -> bool:
        return self.db.exists(self.user_email_key(email))

    def username_exists(self, username: str) -> bool:
        return self.db.exists(self.user_username_key(username))

    def get_user_by_id(self, id: str) -> User:
        data = self.db.get(self.get_user_key(id))
        if data is None:
            raise Exception("User not found")
        return user_from_dict(json.loads(data))

    def get_user_by_email(self, email: str) -> User:
        id = self.db.get(self.user_email_key(email))
        if id is None:
            raise Exception("User not found")
        return self.get_user_by_id(id)

    def get_user_by_username(self, username: str) -> User:
        id = self.db.get(self.user_username_key(username))
        if id is None:
            raise Exception("User not found")
        return self.get_user_by_id(id)
    
    def get_user_by_email_or_username(self, email_or_username: str) -> User:
        user = self.get_user_by_email(email_or_username)
        if user is None:
            user = self.get_user_by_username(email_or_username)
        if user is None:
            raise Exception("User not found")
        return user
