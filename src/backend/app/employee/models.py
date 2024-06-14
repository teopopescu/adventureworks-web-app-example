from sqlalchemy import Column, DateTime, Integer, String, Float
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class Employee(Base):
    __tablename__ = "employee"
    __table_args__ = {"schema": "humanresources"}

    nationalidnumber = Column(Integer, primary_key=True, index=True)
    jobtitle=Column(String)
    # gender=Column(String)
    # hire_date=Column(DateTime)
    # vacation_hours=Column(Float)
    # current_flag=Column(String)
    # org_level=Column(String)
    # organization=Column(String)
    def to_json(self, show_sequences=True):
        return {
            "id": self.nationalidnumber,
            "job_title": self.jobtitle
        }
