import datetime as dat
import sqlalchemy as sa


import database as dt


class Employees(dt.Base):
    __tablename__ = "employees"
    id = sa.Column(sa.Integer, primary_key=True, autoincrement=True)
    name = sa.Column(sa.String, index=True)
    age = sa.Column(sa.Integer, index=True)
    email = sa.Column(sa.String, unique=True, index=True)
    salary = sa.Column(sa.Integer, index=True)
    phone_number = sa.Column(sa.String, unique=True, index=True)
    #id = sa.Column(sa.Integer, primary_key=True, index=True)
    date = sa.Column(sa.DateTime, default=dat.datetime.now)

