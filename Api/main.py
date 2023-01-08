from typing import List
from sqlalchemy import select
from fastapi import Depends, FastAPI, HTTPException
from sqlalchemy.orm import Session
from sqlRelation.db import engine, SessionLocal, conn
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
@app.post("/usuario/", response_model= schemas.createUser)
def creat_user(user: schemas.createUser, db: Session= Depends(get_db)):
    db_usuario = CRUD.create_usuario(db, user=user)
    if db_usuario:
        raise HTTPException(status_code=400, detail=" Usuario já foi criado")
    return CRUD.create_usuario(db=db, user=user)
# ta retornando cod 400 tenho que consertar

# @app.get("/teste/", response_model= schemas.putUser)
# def putUser(cod: int, db: Session = Depends(get_db)):
#     db_usuario = CRUD.updateUser(db = db, cod=cod)
#     return  db_usuario
@app.get("/usuarios/", response_model=list[schemas.Correntista_nome])
async def getUsuarios(s: int = 0, l: int = 100, db: Session = Depends(get_db)):
    usuarios = CRUD.getTodos(db, skip=s, limit=l)
    return usuarios
@app.get("/usuario/")
def readUsuario(cod: int , db: Session = Depends(get_db)):
    db_user = CRUD.get_usuario(db, cod=cod )
    if db_user is None:
        raise HTTPException(status_code=404, detail="usuario não encontrado")
    return  db_user
@app.get("/testeGet/{cod}") ## o schema não é obrigatório
async def getTestadooo(cod: int,db: Session = Depends(get_db)):
    db_user = CRUD.getTeste(db=db, cod=cod)
    return db_user.fetchall()

@app.put("/updatecorrentista/{cod}", response_model=schemas.putUser) #sem o schema ele retorna 200, mas com o schema ele da erro
async def alterar_usuario(cod: int, user: schemas.putUser, db: Session=Depends(get_db)):
    db_user = CRUD.put_user(db=db,user=user,cod=cod)
    return db_user


@app.get("/movimentacoes/", response_model=list[schemas.getMovimetancoes])
async def getMovimentacoes(s: int=0, l:int = 100, db: Session = Depends(get_db)):
    movimentacoes = CRUD.getMovimentacoes(db, skip=s, limit=l)
    return movimentacoes
@app.get("/movimentacao/{cod}", response_model=schemas.getMovimentacao)
async def get_movimentacao(cod: int, db: Session = Depends(get_db)):
    db_moving = CRUD.getMovimentacao(db, cod= cod)
    if db_moving  is None:
        raise HTTPException(status_code=404, detail="Movimentacao não encontrada")
    print(db_moving)
    return db_moving

# serviçoes

# post deposito -- usa  a procedure de deposito EXEC
# post saque -- usa  a procedure de saque EXEC
#post pagamento -- usa a procedure de pagamento EXEC
# post trasnferencia -- faz de um cod_origem -> para um cod_origem usa a procedure EX spTransferencia
#get extrato -- data inicial -> data final -> executa a procedure spExtrato
#put corretnista --- faz um update me correntista e altera os valores das colunas busca feita com where cod_
#Em cenários de CRUD, o PUT normalmente é usado para atualizar algo e o POST para criar (ou fazer outras operações que não se encaixa no CRUD básico), assim como o GET é usado para ler, e o DELETE obviamente para apagar
#delete correntista faz DELETE na tabela correntista usando WHere
#