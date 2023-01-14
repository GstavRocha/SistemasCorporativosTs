from urllib.parse import quote_plus
import mysql.connector
from mysql.connector import errorcode
from .access import password

from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

conn = "mysql+pymysql://gustavo:%s@localhost:3306/bancosa" % quote_plus(f"{password}")
engine = create_engine(conn)
SessionLocal = sessionmaker()
SessionLocal.configure(bind=engine)
Base = declarative_base()


conx = mysql.connector.connect(user='gustavo',
                                   password=f'{password}',
                                   host='localhost',
                                   database='bancosa',
                                   port=3306)

cursor = conx.cursor()


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()