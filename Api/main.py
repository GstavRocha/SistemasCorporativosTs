
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
        return {"Servidor": "Online"}
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
    return CRUD.create_usuario(db=db, user=user)

@app.get("/usuarios/", response_model=list[schemas.Correntista_nome])
async def getUsuarios(s: int = 0, l: int = 100, db: Session = Depends(get_db)):
    usuarios = CRUD.getTodos(db, skip=s, limit=l)
    return usuarios

@app.put("/updatecorrentista/{cod}", response_model=schemas.correntistaResponse)
async def alterar_usuario(cod: int, db: Session=Depends(get_db)):
    if not CRUD.verficaUsuario(cod=cod,database=db):
        raise HTTPException(status_code=404, detail="usuário não encontrado")
    user = CRUD.update_usuario(db,cod=cod)
    return user


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
@app.get("/usuarios/")
def callConnector():
    select = "SELECT * FROM tb_correntista"
    cursor.execute(select)
    result = cursor.fetchall()
    return result
@app.get("/movimentacoes/view")
def vw_moving():
    select = f"select * from vw_extratoCorrentista"
    cursor.execute(select)
    result = cursor.fetchall()
    return result
@app.get("/movimentacao/usuario{cod}")
def vw_moving_correntista(cod: int):
    select_vw = f'select * from vw_movimentacao where nome_correntista = {cod}'
    cursor.execute(select_vw)
    result = cursor.fetchone()
    return result
@app.put("/usuario/update/valor{cod}")
def up_usuario(cod: int, valor: int):
    update = f'update tb_correntista set saldo_correntista = {valor} where cod_correntista = {cod}'
    cursor.execute(update)
    conx.commit()
@app.put("/usuario/update/nome{nome}")
def up_usuario(cod: int, nome: str):
    update = f'update tb_correntista set nome_correntista = "{nome}" where cod_correntista = {cod}'
    cursor.execute(update)
    conx.commit()
@app.put("/usuario/update/email{email}")
def up_usuario(cod: int, email: str):
    update = f'update tb_correntista set email_correntista = "{email}" where cod_correntista = {cod}'
    cursor.execute(update)
    conx.commit()
@app.delete("/usuario/delete/usuario")
def del_usuario(cod: int):
    delete = f'delete from tb_correntista where cod_correntista = {cod}'
    cursor.execute(delete)
    conx.commit()
# post deposito -- usa  a procedure de deposito EXEC
# post saque -- usa  a procedure de saque EXEC
#post pagamento -- usa a procedure de pagamento EXEC
# post trasnferencia -- faz de um cod_origem -> para um cod_origem usa a procedure EX spTransferencia
#get extrato -- data inicial -> data final -> executa a procedure spExtrato
#put corretnista --- faz um update me correntista e altera os valores das colunas busca feita com where cod_
#Em cenários de CRUD, o PUT normalmente é usado para atualizar algo e o POST para criar (ou fazer outras operações que não se encaixa no CRUD básico), assim como o GET é usado para ler, e o DELETE obviamente para apagar
#delete correntista faz DELETE na tabela correntista usando WHere
#