from flask_restful import Resource, reqparse
from flask_jwt import jwt_required
import sqlite3
from models.employee import EmployeeModel

class Employee(Resource):
    parser = reqparse.RequestParser()
    parser.add_argument('salary',
                        type=float,
                        required=True,
                        help='Cant be blank')

    parser.add_argument('department_id',
                        type=float,
                        required=True,
                        help='Every employee needs department id')

    #@jwt_required()
    def get(self, name):
        employee=EmployeeModel.find_by_name(name)
        if employee:
            return employee.json()
        return {'message': 'Employee not found'}, 404

    def post(self, name):
        if EmployeeModel.find_by_name(name):
            return {'message': "An employee with name {} already exists".format(name)}, 400
        data = Employee.parser.parse_args()
        employee = EmployeeModel(name, **data)
        try:
            employee.save_to_db()
        except:
            return {"message":"An error occure"},500
        return employee.json(),201

    def delete(self, name):
        employee=EmployeeModel.find_by_name(name)
        if employee:
            employee.delete_from_db()
            return {'message': 'Employee deleted'}
        return {'message': 'Employee not found.'}, 404

    def put(self, name):
        data = Employee.parser.parse_args()
        employee = EmployeeModel.find_by_name(name)
        if employee:
            employee.salary = data['salary']
        else:
            employee = EmployeeModel(name, **data)
        employee.save_to_db()
        return employee.json()

class EmployeeRecord(Resource):
    def get(self):
        return {'employees': list(map(lambda x: x.json(), EmployeeModel.query.all()))}
