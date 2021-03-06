from flask import request, jsonify
from controller import api, session
from database.model import User
from database.schema import user

controller_name = "users"

@api.route(f"/{controller_name}")
def get_users():
    users_schema = user.UserSchema(strict=True, many=True)

    users = session.query(User).all()
    results = users_schema.dump(users)
    print(results)
    return jsonify(results)

@api.route(f"/{controller_name}/<int:user_id>")
def get_user(user_id):
    users_schema = user.UserSchema(strict=True, many=True)

    existing_user = session.query(User).filter(User.id == user_id)
    results = users_schema.dump(existing_user)
    print(results)
    return jsonify(results)

@api.route(f"/{controller_name}", methods=["POST"])
def create_user():
    user_schema = user.UserSchema(strict=True, many=False)
    user_data = request.get_json()

    data = user_schema.load(user_data).data    
    print(data)
    new_user = User(name=data["name"])
    session.add(new_user)
    session.commit()
    
    result = user_schema.dump(new_user)

    return jsonify(result[0])

@api.route(f"/{controller_name}/<int:user_id>", methods=["PUT"])
def update_user(user_id):
    user_schema = user.UserSchema(strict=True, many=False)
    existing_user = session.query(User).filter(User.id == user_id)
    
    user_data = request.get_json()
    print(user_data)
    existing_user.update({"name": user_data["name"]})
    session.commit()

    result = result = user_schema.dump(existing_user)

    return jsonify(result[0])

@api.route(f"/{controller_name}/<int:user_id>", methods=["DELETE"])
def delete_user(user_id):
    existing_user = session.query(User).filter(User.id == user_id)
    session.delete(existing_user)
    session.commit()

    return ""