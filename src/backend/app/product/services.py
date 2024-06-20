
from src.backend.app.employee.models import Employee


# add classmethod and staticmethod


class EmployeeService:
    @classmethod
    def get_all(cls, db):
        return db.query(Employee).all()
    

    @classmethod
    def get_by_id(cls, db, employee_id):
        return db.query(Employee).filter(Employee.nationalidnumber == employee_id).first()
