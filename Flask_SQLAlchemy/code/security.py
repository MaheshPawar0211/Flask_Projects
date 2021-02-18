from models.user import User_models


def authenticate(username, password):
    user = User_models.find_by_username(username)
    if user and user.password == password:
        return user

def identity(payload):
    user_id = payload['identity']
    return User_models.find_by_id(user_id)
