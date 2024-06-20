from typing import Optional, List

from fastapi import Depends, HTTPException, APIRouter
from sqlalchemy.orm import Session
from src.backend.settings.db import get_db
from src.backend.app.employee.services import EmployeeService
from src.backend.app.employee.schemas import Employee, AddEmployee, UpdateEmployee, DeleteEmployeeRequest,DeleteEmployeeResponse
import logging

logging.basicConfig(level=logging.DEBUG)


employee_router = APIRouter()


@employee_router.get("/employees/{employee_id}")
async def get_employee(
    employee_id: str,
    db: Session = Depends(get_db),
    limit: Optional[int] = 1000,
):
    employee = EmployeeService.get_by_id(db=db, employee_id=employee_id)
    if not employee:
        raise HTTPException(
            status_code=404, detail=f"The employee {employee_id} doesn't exist"
        )
    
    return {
            "job_title": employee.nationalidnumber,
            "national_id_number": employee.jobtitle
        }

@employee_router.post("/employees/")
async def add_employee(
    national_id_number: Optional[str],
    business_entity_id: Optional[str],
    db: Session = Depends(get_db),
    limit: Optional[int] = 1000,
    job_title: Optional[str] = "Chief False Officer",
    login_id: Optional[str] = "1",
    birth_date: Optional[str] = "1994-09-15",
    marital_status: Optional[str] = "M",
    gender: Optional[str] = "M",
    hire_date: Optional[str] = "2021-05-10",


):
    
    """ 
    post national id number
    login id
    job title
    gender
    marital status
    hiredate
    vacationhours


    """
    # EmployeeService.create_employee(db, employee)


    employee = EmployeeService.create_employee(
        db=db, nationalidnumber=national_id_number,jobtitle=job_title,businessentityid=business_entity_id,loginid=login_id, birthdate=birth_date,maritalstatus=marital_status,gender=gender,hiredate=hire_date
    )

    # EmployeeService.create_employee(db, employee)
    return {
            "job_title": employee.nationalidnumber,
            "national_id_number": employee.jobtitle,
            "business_entity_id": employee.businessentityid
        }




@employee_router.put(
    "/employee/{employee_id}",
    response_model=UpdateEmployee,
)
async def update_employee(
    destination_employee_id: int,
    payload: UpdateEmployee,
    db: Session = Depends(get_db),
):
    destination_employee_id = EmployeeService.get_by_id(db=db, employee_id=destination_employee_id)

    if not destination_employee_id:
        raise HTTPException(
            status_code=404,
            detail=f"The employee {destination_employee_id} doesn't exist",
        )

    experiments_groups_list = {p.experiment_id: p.group_id for p in payload.experiments}
    EmployeeService.update_by_employee_id(
            db=db, employee=payload.employee_id
        )
    
    # for entry in payload.experiments:

    #     employee = EmployeeService.get_by_id(db, employee_id=entry.employee_id)

    #     if not group:
    #         raise HTTPException(
    #             status_code=404, detail=f"The group: {entry.group_id} doesn't exists"
    #         )

    #     EmployeeService.update_by_employee_id(
    #         db=db, experiment=payload.experiments, from_group=group, to_group=destination_group
    #     )

    return {
        "success": True,
        "employee_id": destination_employee_id.to_json(),
    }

@employee_router.delete(
    "/employee/{group_id}", response_model=DeleteEmployeeResponse
)
async def delete_experiments_from_the_group(
    group_id: int,
    entry: DeleteEmployeeRequest,
    db: Session = Depends(get_db),
):
    employee = EmployeeService.get_by_id(db=db, group_id=group_id)

    if not employee:
        raise HTTPException(
            status_code=404, detail=f"The employee: {employee} doesn't exist"
        )

    EmployeeService.delete_employee(db, employee, entry.experiments)
    return {"success": True, "employee_removed": entry.employee}
