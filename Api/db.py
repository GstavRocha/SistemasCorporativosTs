from urllib.parse import quote_plus
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

connDB = "mysql + pymysql://gustavo"