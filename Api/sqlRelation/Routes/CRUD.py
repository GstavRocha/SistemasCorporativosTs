from sqlalchemy.orm import Session
from ..DataBase import models, schemas


def get_usuario(db: Session, cod: int):
    return db.query(models.Correntista).filter(models.Correntista.cod_correntista == cod).first()
def getTodos(db: Session, skip: int =0, limit: int = 100):
    return db.query(models.Correntista).offset(skip).limit(limit).all()
def usuarioNome(db: Session):
    return db.query(models.Correntista).filter(models.Correntista.nome_correntista).all()

def create_usuario(db: Session,user: schemas.Correntista_Schema):
    usuario_db = models.Correntista(
        nome_correntista= user.nome_correntista,
        email_correntista= user.email_correntista,
        saldo_correntista= user.saldo_correntista)
    db.add(usuario_db)
    db.commit()
    db.refresh(usuario_db)
    return usuario_db
