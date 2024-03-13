from typing import List
import Schema
import database as dt
import model


def add_table():
    return dt.Base.metadata.create_all(bind=dt.engine)


def create_emp(emp: Schema.Employee, db: dt.SessionLocal):
    emp = model.Employees(**emp.dict())
    db.add(emp)
    db.commit()
    db.refresh(emp)
    return Schema.Employee.from_orm(emp)


async def get_all_data(db: dt.SessionLocal) -> List[Schema.Employee]:
    ct = db.query(model.Employees).all()
    return list(map(Schema.Employee.from_orm, ct))


async def get_emp_by_id(db: dt.SessionLocal, emp_id: int):
    emp = db.query(model.Employees).filter(model.Employees.id == emp_id).first()
    return emp


async def delete_emp(db: dt.SessionLocal, emp=model.Employees):
    db.delete(emp)
    db.commit()


async def update_emp(db: dt.SessionLocal, emp_data: Schema.Employee, emp: model.Employees):
    emp.name = emp_data.name
    emp.salary = emp_data.salary
    emp.age = emp_data.age
    emp.phone = emp_data.phone_number
    emp.email = emp_data
    db.commit()
    db.refresh(emp)
    return Schema.Employee.from_orm(emp)
