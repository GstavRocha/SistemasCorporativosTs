from sqlalchemy.orm import Session
from ..DataBase import models, schemas
from sqlalchemy import select,values,insert,update
import pymysql.cursors
from ..db import conn


def get_usuario(db: Session, cod: int):
    return db.query(models.Correntista).filter(models.Correntista.cod_correntista == cod).first()
def getTodos(db: Session, skip: int =0, limit: int = 100):
    return db.query(models.Correntista).offset(skip).limit(limit).all()
def usuarioNome(db: Session):
    return db.query(models.Correntista).filter(models.Correntista.nome_correntista).all()

def getTeste(db: Session, cod: int):
    return db.execute(select(models.Correntista).where(models.Correntista.cod_correntista== cod))

def put_user(db: Session, user: schemas.putUser,cod: int):
    usuario_db = db.execute(update(models.Correntista).values(
        nome_correntista=user.nome_correntista,
        email_correntista=user.email_correntista
    ).where(models.Correntista.cod_correntista == cod))
    return usuario_db

# def putUsuario(db: Session, cod: int, user: schemas.putUser):
#     usuario_db = db.query(models.Correntista).filter(models.Correntista.cod_correntista == cod)
#     usuario_db_put = models.Correntista(
#         nome_correntista= user.nome_correntista,
#         email_correntista= user.email_correntista)
def getMovimentacoes(db: Session, skip: int =0 , limit: int =100):
    return db.query(models.Movimentacao).offset(skip).limit(limit).all()

def getMovimentacao(db: Session, cod: int):
    return db.query(models.Movimentacao).filter(models.Movimentacao.cod_movimentacao == cod).first()

def create_usuario(db: Session, user: schemas.createUser):
    usuario_db = models.Correntista(
        nome_correntista= user.nome_correntista,
        email_correntista= user.email_correntista,
        saldo_correntista= user.saldo_correntista)
    db.add(usuario_db)
    db.commit()
    db.refresh(usuario_db)
    return usuario_db
