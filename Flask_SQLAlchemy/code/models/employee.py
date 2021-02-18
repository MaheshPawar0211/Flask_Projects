from db import db

class EmployeeModel(db.Model):
    __tablename__="employees"

    id=db.Column(db.Integer,primary_key=True)
    name=db.Column(db.String(80))
    salary = db.Column(db.Float(precision=2))
    department_id=db.Column(db.Integer,db.ForeignKey('departments.id'))
    department=db.relationship('DepartmentModel')

    def __init__(self,name,salary,department_id):
        self.name=name
        self.salary=salary
        self.department_id=department_id

    def json(self):
        return {'name':self.name,'salary':self.salary}

    @classmethod
    def find_by_name(cls,name):
        return cls.query.filter_by(name=name).first()

    def save_to_db(self):
        db.session.add(self)
        db.session.commit()

    def delete_from_db(self):
        db.session.delete(self)
        db.session.commit()
