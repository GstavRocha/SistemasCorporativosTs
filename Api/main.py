import errno

from fastapi import Depends, FastAPI, HTTPException, requests, APIRouter
from fastapi.encoders import jsonable_encoder
from sqlalchemy.orm import Session
from .sqlRelation.db import engine, SessionLocal, conn,get_db,conx, cursor
from .sqlRelation.DataBase import models, schemas
from .sqlRelation.Routes import CRUD
models.Base.metadata.create_all(bind=engine)
app = FastAPI()
appRouter = APIRouter

database = models.Correntista()
@app.get("/")
async def serveLoad():
        return HTTPException(status_code=200, detail="Servidor On",headers=None)
@app.get("/usuario/{cod}")
def verifica_usuario(cod: int , db: Session = Depends(get_db)):
    db_user = CRUD.verficaUsuario(db, cod=cod )
    if db_user is None:
        raise HTTPException(status_code=404, detail="usuario não encontrado")
    else:
        db_user = HTTPException(status_code=200, detail="usuario encontrado", headers=db_user)
        return db_user
@app.post("/usuario/", response_model= schemas.createUser)
def creat_user(user: schemas.createUser, db: Session= Depends(get_db)):
    db_usuario = CRUD.create_usuario(db, user=user)
    if db_usuario:
        raise HTTPException(status_code=400, detail=" Usuario já foi criado")
    return CRUD.create_usuario(databbase=db, user=user)

@app.get("/usuarios/", response_model=list[schemas.Correntista_nome])
async def getUsuarios(s: int = 0, l: int = 100, db: Session = Depends(get_db)):
    usuarios = CRUD.getTodos(db, skip=s, limit=l)
    return usuarios
@app.get("/usuarios/clube")
def callConnector():
    select = "SELECT * FROM tb_correntista"
    cursor.execute(select)
    result = cursor.fetchall()
    return HTTPException(status_code=200, detail="Sucess", headers=result)

@app.put("/usuario/update/valor{cod}")
def up_usuario(cod: int, valor: int):
    update = f'update tb_correntista set saldo_correntista = {valor} where cod_correntista = {cod};'
    confere = f'select * from tb_correntista where cod_correntista = {cod};'
    cursor.execute(update)
    cursor.execute(confere)
    verif = cursor.fetchall()
    conx.commit()
    return HTTPException(status_code=200, detail="SUCESS", headers=verif)
@app.put("/usuario/update/nome{nome}")
def up_usuario(cod: int, nome: str):
    update = f'update tb_correntista set nome_correntista = "{nome}" where cod_correntista = {cod};'
    confere = f'select * from tb_correntista where cod_correntista = {cod};'
    cursor.execute(update)
    cursor.execute(confere)
    verif = cursor.fetchall()
    conx.commit()
    return HTTPException(status_code=200, detail="SUCESS", headers=verif)

@app.put("/usuario/update/email{email}")
def up_usuario(cod: int, email: str):
    update = f'update tb_correntista set email_correntista = "{email}" where cod_correntista = {cod};'
    confere = f'select * from tb_correntista where cod_correntista = {cod};'
    cursor.execute(update)
    cursor.execute(confere)
    verif = cursor.fetchall()
    conx.commit()
    conx.close()
    return HTTPException(status_code=200, detail="SUCESS", headers=verif)
@app.get("/movimentacoes/view")
def vw_moving():
    select = f"select * from vw_extratoCorrentista;"
    cursor.execute(select)
    result = cursor.fetchall()
    return HTTPException(status_code=200, detail="Sucess", headers=result)


@app.get("/movimentacoes/", response_model=list[schemas.getMovimetancoes])
async def getMovimentacoes(s: int=0, l:int = 100, db: Session = Depends(get_db)):
    movimentacoes = CRUD.getMovimentacoes(db, skip=s, limit=l)
    return movimentacoes
@app.get("/movimentacao/correntista/{cod}")
def moving_correntista(cod: int):
    vw_correntista_moving = f"select * from vw_extratoCorrentista where cod_correntista = {cod}"
    cursor.execute(vw_correntista_moving)
    result = cursor.fetchall()
    if result == []:
        raise HTTPException(status_code=422, detail="Usuario não identificado")
    return HTTPException(status_code=200, detail="Sucess", headers=result)

@app.post("/usuario/deposito/{cod}{valor}")
def deposito(cod: int, valor: float):
    sp_deposito = f'CALL sp_deposito({cod},{valor});'
    confere = f'select * from tb_movimentacao where cod_correntista = {cod}'
    cursor.execute(sp_deposito)
    verif =cursor.execute(confere)
    cursor.fetchall()
    conx.commit()
    return verif
@app.post("/usuario/pagamento/{cod}{valor}")
def pagamento(cod: int, valor: float):
    sp_pagamento = f'CALL sp_pagamento({cod},{valor})'
    cursor.execute(sp_pagamento)
    conx.commit()

@app.delete("/usuario/delete/usuario")
def del_usuario(cod: int):
    delete = f'delete from tb_correntista where cod_correntista = {cod}'
    cursor.execute(delete)
    conx.commit()
    conx.close()
# post deposito -- usa  a procedure de deposito EXEC
# post saque -- usa  a procedure de saque EXEC
#post pagamento -- usa a procedure de pagamento EXEC
# post trasnferencia -- faz de um cod_origem -> para um cod_origem usa a procedure EX spTransferencia
#get extrato -- data inicial -> data final -> executa a procedure spExtrato
#put corretnista --- faz um update me correntista e altera os valores das colunas busca feita com where cod_
#Em cenários de CRUD, o PUT normalmente é usado para atualizar algo e o POST para criar (ou fazer outras operações que não se encaixa no CRUD básico), assim como o GET é usado para ler, e o DELETE obviamente para apagar
#delete correntista faz DELETE na tabela correntista usando WHere
#