from sqlalchemy.orm import Session
from ..DataBase import models, schemas


def get_usuario(db: Session, nome: str):
    return db.query(models.Correntista).filter(models.Correntista.nome_correntista == nome).first()
def getTodos(db: Session, skip: int =0, limit: int = 100):
    return db.query(models.Correntista).offset(skip).limit(limit).all()

def create_usuario(db: Session,user: schemas.Correntista_Schema):
    usuario_db = models.Correntista(
        nome_correntista= user.nome,
        email_correntista= user.email,
        saldo_correntista= user.saldo)
    db.add(usuario_db)
    db.commit()
    db.refresh(usuario_db)
    return usuario_db
