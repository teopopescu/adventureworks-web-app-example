
from src.backend.app.employee.models import Employee


# add classmethod and staticmethod


class EmployeeService:
    @classmethod
    def get_all(cls, db):
        return db.query(Employee).all()
    

    @classmethod
    def get_by_id(cls, db, employee_id):
        return db.query(Employee).filter(Employee.nationalidnumber == employee_id).first()
    

    @classmethod
    def create_employee(self, db, **kwargs):
        instance = Employee(**kwargs)
        db.add(instance)
        db.commit()
        return instance
    
    """ 
    businessentityid | nationalidnumber |         loginid          |             jobtitle              | birthdate  | maritalstatus | gender |  hiredate  | salariedflag | vacationhours | sickleavehours | currentflag |               rowguid                |    modifieddate     | organizationnode 
    """

    @classmethod
    def update_employee(cls, db, employee_id):
        return db.query(Employee).filter(Employee.nationalidnumber == employee_id).first()
    
    @classmethod
    def delete_employee(cls, db, employee_id):
        return db.query(Employee).filter(Employee.nationalidnumber == employee_id).first()
    
    @classmethod
    def get_employee_by_fields(cls, db, employee_id):
        return db.query(Employee).filter(Employee.nationalidnumber == employee_id).first()
