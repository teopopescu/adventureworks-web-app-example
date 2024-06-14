from typing import Optional, List

from fastapi import Depends, HTTPException, APIRouter
from sqlalchemy.orm import Session
from src.backend.settings.db import get_db
from src.backend.app.employee.services import EmployeeService
from src.backend.app.employee.schemas import EmployeeResponse


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
