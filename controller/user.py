from controller import api, session
from database.model import User

@api.route("/user")
def get_users():
    #users = session.query(User).all()
    ##print(users)
    #print(users[0])
    #print("hello")
    return "Get all users"

@api.route("/user", methods=["POST"])
def create_user():
    return "Create user"

@api.route("/user/<uuid:user_id>", methods=["PUT"])
def update_user(user_id):
    return f"Update user {user_id}"

@api.route("/user/<uuid:user_id>", methods=["DELETE"])
def delete_user(user_id):
    return f"Deleting user {user_id}"