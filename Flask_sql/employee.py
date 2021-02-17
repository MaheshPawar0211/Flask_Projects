from flask_restful import Resource, reqparse
from flask_jwt import jwt_required
import sqlite3


class Employee(Resource):
    parser = reqparse.RequestParser()
    parser.add_argument('salary',
                        type=float,
                        required=True,
                        help='Cant be blank')
    @classmethod
    def find_by_name(cls,name):
        connection = sqlite3.connect('data.db')
        cursor = connection.cursor()
        query = "SELECT * FROM employee WHERE name=?"
        result = cursor.execute(query, (name,))
        print(result)
        row = result.fetchone()
        print('row',row)
        connection.close()
        if row:
            return {'employee':{'name':row[0],'salary':row[1]}}

    @jwt_required()
    def get(self, name):
        employee=self.find_by_name(name)
        if employee:
            return employee
        return {'message': 'Employee not found'}, 404

    def post(self, name):
        # Check if employee alrady exisit in list if not add it to list
        if self.find_by_name(name):
            return {'message': "An employee with name {} already exists".format(name)}, 400
        data = Employee.parser.parse_args()
        # data=request.get_json()
        employee = {'name': name, 'salary': data['salary']}
        try:
            self.insert(employee)
        except:
            return {"message":"An error occure"},500
        return employee,200

    @classmethod
    def insert(cls,employee):
        connection = sqlite3.connect('data.db')
        cursor = connection.cursor()
        query="INSERT INTO employee VALUES (?,?)"
        cursor.execute(query,(employee['name'],employee['salary']))
        connection.commit()
        connection.close()

    def delete(self, name):
        connection = sqlite3.connect('data.db')
        cursor = connection.cursor()
        query="DELETE FROM employee WHERE name= ?"
        cursor.execute(query,(name,))
        connection.commit()
        connection.close()
        return {'message': 'Employee deleted'}

    def put(self, name):
        data = Employee.parser.parse_args()
        # data=request.get_json()
        employee = self.find_by_name(name)
        updated_employee = {'name': name, 'salary': data['salary']}
        if employee is None:
            try:
                self.insert(updated_employee)
            except:
                return {"message":"An error occurred while inserting employee."},500
        else:
            self.update(updated_employee)
        return updated_employee

    @classmethod
    def update(cls,employee):
        connection = sqlite3.connect('data.db')
        cursor = connection.cursor()
        query="UPDATE employee SET salary=? WHERE name=?"
        cursor.execute(query,(employee['salary'],employee['name']))
        connection.commit()
        connection.close()

class EmployeeRecord(Resource):
    def get(self):
        connection = sqlite3.connect('data.db')
        cursor = connection.cursor()
        query="select * from employee"
        result=cursor.execute(query)
        employees=[]
        for row in result:
            employees.append({'name':row[0],'salary':row[1]})
        connection.close()
        return {'employees':employees}
