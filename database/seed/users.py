from database.model import User

def seed_users():
    return [
        User(name="seed_user_1"),
        User(name="seed_user_2"),
    ]