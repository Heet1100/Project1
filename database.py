import sqlalchemy as sa
import sqlalchemy.ext.declarative as dec
import sqlalchemy.orm as orm

Data_Base = "postgresql://postgres:root@localhost/company"
engine = sa.create_engine(Data_Base)
SessionLocal = orm.sessionmaker(bind=engine, autocommit=False, autoflush=False)
Base = dec.declarative_base()
