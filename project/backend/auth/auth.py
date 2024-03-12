from flask import Blueprint, request, jsonify, session
from flask_bcrypt import Bcrypt

from redis_db import redis_db
from store.user import UserStore, User


auth = Blueprint("auth", __name__, url_prefix="/auth")
bcrypt = Bcrypt()
user_store = UserStore(redis_db)


@auth.route("/register", methods=["POST"])
def register():
    data: dict = request.json
    username = data.get("username")
    account_name = data.get("email")
    password = data.get("password")

    if not account_name or not password:
        return jsonify({"error": "Email and password are required"}), 400
    if user_store.email_exists(account_name):
        return jsonify({"error": "Email already exists"}), 400
    if user_store.username_exists(account_name):
        return jsonify({"error": "Username already exists"}), 400

    try:
        hashed_password = bcrypt.generate_password_hash(password).decode("utf-8")
        user_store.create_user(username, account_name, hashed_password)
    except Exception as e:
        return jsonify({"error": str(e)}), 500

    return jsonify({"message": "User registered successfully"})


@auth.route("/signin", methods=["POST"])
def signin():
    data = request.json
    account_name = data.get("email")
    password = data.get("password")

    if not account_name or not password:
        return jsonify({"error": "Email and password are required"}), 400

    try:
        user = user_store.get_user_by_email_or_username(account_name)
        pass
    except Exception as e:
        return jsonify({"error": str(e)}), 500

    if not bcrypt.check_password_hash(user.password, password):
        return jsonify({"error": "Invalid password"}), 401

    return jsonify({"message": "User signed in successfully"})


@auth.route("/logout", methods=["GET"])
def logout():
    session.pop("email", None)
    return jsonify({"message": "Logged out successfully"}), 200
