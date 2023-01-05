from typing import List
from fastapi.encoders import jsonable_encoder
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
@app.get("/usuarios/", response_model=list[schemas.Correntista_nome])
async def getUsuarios(s: int = 0, l: int = 100, db: Session = Depends(get_db)):
    usuarios = CRUD.getTodos(db, skip=s, limit=l)
    return usuarios
@app.get("/usuario/", response_model= schemas.Correntista_nome)
def readUsuario(cod: int , db: Session = Depends(get_db)):
    db_user = CRUD.get_usuario(db, cod=cod )
    if db_user is None:
        raise HTTPException(status_code=404, detail="usuario não encontrado")
    return  db_user
# serviçoes
# get movimentacao -- faz o select em todas as movimentacoes
# post correntista -- crea um usuario especifico
# post deposito -- usa  a procedure de deposito EXEC
# post saque -- usa  a procedure de saque EXEC
#post pagamento -- usa a procedure de pagamento EXEC
# post trasnferencia -- faz de um cod_origem -> para um cod_origem usa a procedure EX spTransferencia
#get extrato -- data inicial -> data final -> executa a procedure spExtrato
#get correntista - faz um select no cod_correntista e um where no id
#get movimentacao -- faz um select em movimentacao e um where no cod_movimentacao
#put corretnista --- faz um update me correntista e altera os valores das colunas busca feita com where cod_
#