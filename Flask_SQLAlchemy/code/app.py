from flask import Flask
from flask_restful import Api
from flask_jwt import JWT

from security import authenticate,identity
from resources.user import UserRegister
from resources.employee import Employee,EmployeeRecord
from resources.department import Department,DepartmentRecord


app = Flask(__name__)
app.secret_key='jose'
api = Api(app)

@app.before_first_request
def create_tables():
    db.create_all()

jwt=JWT(app,authenticate,identity)
app.config['SQLALCHEMY_DATABASE_URI']='sqlite:///data.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS']=False
# REST API return resource => Resource is class

api.add_resource(Department,'/department/<string:name>')
api.add_resource(Employee,'/employee/<string:name>')
api.add_resource(EmployeeRecord,'/employees')
api.add_resource(DepartmentRecord,'/departments')
api.add_resource(UserRegister,'/register')
if __name__=='__main__':
    from db import db
    db.init_app(app)
    app.run(port=5000,debug=True)

