from typing import List
from fastapi import Depends, FastAPI, HTTPException
from sqlalchemy.orm import Session
from sqlRelation.db import engine, SessionLocal
from sqlRelation.DataBase import models, schemas
from sqlRelation.Routes import CRUD
models.Base.metadata.create_all(bind=engine)
app = FastAPI()
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
@app.get("/")
async def serveLoad():
        return {"Servidor": "Online"}
@app.get("/usuarios/", response_model=list[schemas.Correntista_Schema])
async def getUsuarios(s: int = 0, l: int = 100, db: Session = Depends(get_db)):
    usuarios = CRUD.getTodos(db, skip=s, limit=l)
    return usuarios

