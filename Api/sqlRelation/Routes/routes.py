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
def taRodando():
    return {"teste": "funciona"}

@app.get("/usuario/", response_model=list[schemas.listaUsuario])
async def todos(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    user = CRUD.getTodos(db,skip=skip, limit=limit)
    return user

@app.post("/usuario/", response_model= schemas.Correntista_Schema)
def crearUsuario(user: schemas.Correntista_Schema, db: Session = Depends(get_db)):
    user_db = CRUD.create_usuario(db, user = user)
    if user_db:
        error = HTTPException(status_code=400 , detail="Já cadastrado")
        raise error
    return CRUD.create_usuario(db=db, user=user) #tem que ter um wait;
# @app.get("/usuario/", response_model= schemas.Saldo)
# async def
