from flask import Flask
from flask_restful import Api
from flask_jwt import JWT
from security import authenticate,identity
from user import UserRegister
from employee import Employee,EmployeeRecord
app = Flask(__name__)
app.secret_key='jose'
api = Api(app)

jwt=JWT(app,authenticate,identity)

# REST API return resource => Resource is class

api.add_resource(Employee,'/employee/<string:name>')
api.add_resource(EmployeeRecord,'/employees')
api.add_resource(UserRegister,'/register')
app.run(port=5000,debug=True)

