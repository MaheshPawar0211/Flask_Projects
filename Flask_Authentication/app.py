from flask import Flask, request
from flask_restful import Resource, Api, reqparse
from flask_jwt import JWT,jwt_required
from  security import authenticate,identity
app = Flask(__name__)
app.secret_key='jose'
api = Api(app)

jwt=JWT(app,authenticate,identity)

employees = []


# REST API return resource => Resource is class

class Employee(Resource):
    parser = reqparse.RequestParser()
    parser.add_argument('salary',
                        type=float,
                        required=True,
                        help='Cant be blank')
    @jwt_required()
    def get(self, name):
        employee = next(filter(lambda x: x['name'] == name, employees), None)
        return {'employee': employee}, 200 if employee else 404

    def post(self, name):
        # Check if employee alrady exisit in list if not add it to list
        if (next(filter(lambda x: x['name'] == name, employees), None)) is not None:
            return {'message': "An employee with name {} already exists".format(name)}, 400
        data = Employee.parser.parse_args()
        # data=request.get_json()
        employee = {'name': name, 'salary': data['salary']}
        employees.append(employee)
        return employees

    def delete(self, name):
        global employees
        employees = list(filter(lambda x: x['name'] != name, employees))
        return {'message': 'Item deleted'}

    def put(self, name):
        data = Employee.parser.parse_args()
        # data=request.get_json()
        employee = next(filter(lambda x: x['name'] == name, employees), None)
        if employee is None:
            employee = {'name': name, 'salary': data['salary']}
            employees.append(employee)
        else:
            employee.update(data)
        return employee


class EmployeeRecord(Resource):
    def get(self):
        return {'employees': employees}


api.add_resource(Employee, '/employee/<string:name>')
api.add_resource(EmployeeRecord, '/employees')
app.run(port=5000,debug=True)

