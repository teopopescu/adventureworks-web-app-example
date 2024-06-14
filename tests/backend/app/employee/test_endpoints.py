from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.orm import Session
from unittest.mock import MagicMock, patch
import pytest
from typing import Optional
from fastapi.testclient import TestClient
app = FastAPI()


client = TestClient(app)

# Mock dependencies
class MockEmployee:
    def __init__(self, jobtitle, nationalidnumber):
        self.jobtitle = jobtitle
        self.nationalidnumber = nationalidnumber

class EmployeeService:
    @staticmethod
    def get_by_id(db, employee_id):
        if employee_id == "existing_id":
            return MockEmployee(jobtitle="Developer", nationalidnumber="12345")
        return None

def get_db():
    pass  # Mock the dependency injection of the database session

# Test cases
@pytest.mark.asyncio
async def test_get_employee_success():
    response = client.get("/employees/existing_id")
    assert response.status_code == 200
    assert response.json() == {
        "job_title": "Developer",
        "national_id_number": "12345"
    }

@pytest.mark.asyncio
async def test_get_employee_not_found():
    response = client.get("/employees/non_existing_id")
    assert response.status_code == 404
    assert response.json() == {"detail": "The employee non_existing_id doesn't exist"}

# Running the tests
if __name__ == "__main__":
    pytest.main()
