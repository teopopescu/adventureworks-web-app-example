from typing import List, Optional

from pydantic import BaseModel, Field

    
class EmployeeResponse(BaseModel):
    nationalidnumber: str
    jobtitle: str
    # gender: str
    # hire_date: str
    # vacation_hours: float
    # current_flag: str
    # org_level: str
    # organization: str
