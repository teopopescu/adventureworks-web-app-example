from typing import List, Optional

from pydantic import BaseModel, Field


class Employee(BaseModel):
    national_id_number: str
    jobtitle: str
    
class EmployeeResponse(BaseModel):
    nationalidnumber: str
    jobtitle: str
    # gender: str
    # hire_date: str
    # vacation_hours: float
    # current_flag: str
    # org_level: str
    # organization: str


class AddEmployee(BaseModel):
    success: Optional[bool]
    employee_added: Optional[Employee]


class UpdateEmployee(BaseModel):
    success: bool
    employee_updated: Employee

class DeleteEmployeeRequest(BaseModel):
    success: bool
    employee_deleted: Employee

class DeleteEmployeeResponse(BaseModel):
    success: bool
    employee_deleted: Employee

