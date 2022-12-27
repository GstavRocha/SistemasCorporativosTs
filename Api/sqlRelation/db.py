from urllib.parse import quote_plus
from .access import password

from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

conn = "mysql+pymysql://gustavo:%s@localhost:3306/bancosa" % quote_plus(f"{password}")
engine = create_engine(conn)
SessionLocal = sessionmaker()
SessionLocal.configure(bind=engine)
Base = declarative_base()
