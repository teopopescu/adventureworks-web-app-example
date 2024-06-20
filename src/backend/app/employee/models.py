from sqlalchemy import Column, DateTime, Integer, String, Float
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class Employee(Base):
    __tablename__ = "employee"
    __table_args__ = {"schema": "humanresources"}
    businessentityid = Column(Integer)
    nationalidnumber = Column(Integer, primary_key=True, index=True)
    jobtitle=Column(String)
    loginid=Column(String)
    birthdate=Column(String)
    maritalstatus=Column(String)
    gender=Column(String)
    hiredate=Column(String)


    def to_json(self, show_sequences=True):
        return {
            "id": self.nationalidnumber,
            "job_title": self.jobtitle
        }
