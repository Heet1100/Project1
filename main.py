from http.client import HTTPException

from fastapi import FastAPI, Depends
from typing import List
from sqlalchemy import orm
import Schema
import Services
from database import SessionLocal
from sqlalchemy.orm import Session
from logger import logger

app = FastAPI()
logger.info("Starting the API...")


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@app.post("/api/employee/",response_model=Schema.Employee)
async def create_employee(employee: Schema.Employee, db: Session = Depends(get_db)):
    logger.info("Creating the Employee")
    return Services.create_emp(emp=employee, db=db)


@app.get("/api/employee/", response_model=List[Schema.Employee])
async def get_emp(db: Session = Depends(get_db)):
    logger.info("Retrieving the Employee")
    return Services.get_all_data(db)


@app.get("/api/employee/{emp_id}", response_model=Schema.Employee)
async def get_employee(emp_id: int, db: Session = Depends(get_db)):
    logger.info("Retrieving the Employee by id")
    emp = Services.get_emp_by_id(db, emp_id)
    if emp is None:
        logger.info("Employee not found")
        raise HTTPException(404, "Employee not found")
    return Services.get_emp_by_id(db, emp_id)


@app.delete("/api/employee/{emp_id}")
async def delete_emp(emp_id: int, db: orm.Session = Depends(get_db)):
    logger.info("Deleting Employee")
    emp = Services.get_emp_by_id(db, emp_id)
    if emp is None:
        logger.info("Employee not found")
        raise HTTPException(404, "Employee does not exist")
    return Services.delete_emp(emp, db)


@app.put("/api/employee/{emp_id}", response_model=Schema.Employee)
async def update_emp(emp_data: Schema.Employee, emp_id: int, db: orm.Session = Depends(get_db)):
    logger.info("Updating Employee")
    emp = await Services.get_emp_by_id(db, emp_id)
    if emp is None:
        logger.info("Employee not found")
        raise HTTPException(404, "Employee does not exist")
    return await Services.update_emp(db, emp_data, emp)
