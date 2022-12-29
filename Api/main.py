from typing import List
from fastapi import Depends, FastAPI, HTTPException
from sqlalchemy.orm import Session
from sqlRelation.db import engine, SessionLocal
from sqlRelation.DataBase import models, schemas
from sqlRelation.Routes import CRUD
from sqlRelation.Routes import routes
routes.app = FastAPI()