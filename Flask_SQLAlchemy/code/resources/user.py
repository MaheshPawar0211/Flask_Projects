from flask_restful import Resource,reqparse
import sqlite3
from  models.user import User_models


class UserRegister(Resource):
    parser = reqparse.RequestParser()
    parser.add_argument('username',
                        type=str,
                        required=True,
                        help='Cant be blank')
    parser.add_argument('password',
                        type=str,
                        required=True,
                        help='Cant be blank')

    def post(self):
        data=UserRegister.parser.parse_args()
        if User_models.find_by_username(data["username"]):
            return {"message":"User alredy exists"},400
        user=User_models(**data)
        user.save_to_db()
        return {"message":"User Created Sucessfully."},201