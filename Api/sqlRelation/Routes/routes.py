from sqlalchemy.orm import Session
from ..DataBase import models, schemas


def get_usuario(db: Session, nome: str):
    return db.query(models.Correntista).filter(models.Correntista.nome_correntista == nome).first()


def create_usuario(db: Session, user: schemas.Correntista):
    db_user = models.Correntista(nome_correntista=user.nome)
    db.add(db_user)
    db.refresh(db_user)
    return db_user
