import datetime as dat
from pydantic import BaseModel


class BaseEmployee(BaseModel):
    name: str
    age: int
    salary: int
    email: str
    phone_number: str


class Employee(BaseEmployee):
    id: int
    date: dat.datetime

    class Config:
        orm_mode = True
