from sqlalchemy.orm import Session
from ..DataBase import models, schemas
import mysql.connector
from ..db import conn
from sqlalchemy import select,values,insert,update,text
import pymysql.cursors
from ..db import conn

# verifica usuario pelo cod
def verficaUsuario(database: Session, cod: int):
    return database.query(models.Correntista).filter(models.Correntista.cod_correntista == cod).first()
# recebe todos usuarios
def getTodos(databbase: Session, skip: int =0, limit: int = 100):
    return databbase.query(models.Correntista).offset(skip).limit(limit).all()
def usuarioNome(databbase: Session):
    return databbase.query(models.Correntista).filter(models.Correntista.nome_correntista).all()
def save(databbase: Session, user: models.Correntista):
    if user.cod_correntista:
        databbase.merge(user)
    else:
        databbase.add(user)
    databbase.commit()
    return user
def verifica_id(databbase: Session, cod: int) -> models.Correntista:
    return databbase.query(models.Correntista).filter(models.Correntista.cod_correntista == cod).first() is not None
def getTeste(databbase: Session, cod: int):
    return databbase.execute(select(models.Correntista).where(models.Correntista.cod_correntista== cod))
def getMovimentacoes(databbase: Session, skip: int =0 , limit: int =100):
    return databbase.query(models.Movimentacao).offset(skip).limit(limit).all()

def getMovimentacao(databbase: Session, cod: int):
    return databbase.query(models.Movimentacao).filter(models.Movimentacao.cod_movimentacao == cod).first()
def create_usuario(databbase: Session, user: schemas.createUser):
    usuario_db = models.Correntista(
        nome_correntista= user.nome_correntista,
        email_correntista= user.email_correntista,
        saldo_correntista= user.saldo_correntista)
    databbase.add(usuario_db)
    databbase.commit()
    databbase.refresh(usuario_db)
    return usuario_db

# usando mysql.connector








