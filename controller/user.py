from flask import jsonify
from controller import api, session
from database.model import User
from database.schema import user

@api.route("/user")
def get_users():
    user_schema = user.UserSchema(strict=True, many=True)

    users = session.query(User).all()
    results = user_schema.dump(users)
    return jsonify(results)

@api.route("/user", methods=["POST"])
def create_user():
    return "Create user"

@api.route("/user/<int:user_id>", methods=["PUT"])
def update_user(user_id):
    return f"Update user {user_id}"

@api.route("/user/<int:user_id>", methods=["DELETE"])
def delete_user(user_id):
    return f"Deleting user {user_id}"