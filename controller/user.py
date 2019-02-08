from controller import api

@api.route("/user")
def get_users():
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