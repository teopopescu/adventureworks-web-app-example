from sqlalchemy import create_engine
from sqlalchemy.orm import Session

engine = create_engine("postgresql+psycopg2://postgres:mysecretpassword@localhost:5432/Adventureworks")


def get_db():
    return Session(engine)

