from flask_restful import Resource
from models.department import DepartmentModel

class Department(Resource):
    def get(self, name):
        department=DepartmentModel.find_by_name(name)
        if department:
            return department.json()
        return {'message': 'department not found'}, 404

    def post(self, name):
        if DepartmentModel.find_by_name(name):
            return {'message': "A department with name {} already exists".format(name)}, 400
        department = DepartmentModel(name)
        try:
            department.save_to_db()
        except:
            return {"message":"An error occure"},500
        return department.json(),200

    def delete(self, name):
        department=DepartmentModel.find_by_name(name)
        if department:
            department.delete_from_db()
        return {'message': 'department deleted'}

class DepartmentRecord(Resource):
    def get(self):
        return {'departments': list(map(lambda x: x.json(), DepartmentModel.query.all()))}
