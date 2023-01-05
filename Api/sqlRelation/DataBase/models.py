from sqlalchemy import Column, Integer, CHAR,String, Enum, DDL, event, FLOAT, VARCHAR, TIMESTAMP, ForeignKey
from sqlalchemy.orm import relationship
from ..db import Base


class Correntista(Base):
    __tablename__ = "tb_correntista"
    cod_correntista = Column(Integer, primary_key=True)
    nome_correntista = Column(VARCHAR(60))
    email_correntista = Column(VARCHAR(50))
    saldo_correntista = Column(FLOAT)
    chave_fk1 = relationship("Movimentacao", back_populates="chave_fk2")


class Movimentacao(Base):
    __tablename__ = "tb_movimentacao"
    cod_movimentacao = Column(Integer, primary_key=True)
    cod_correntista = Column(Integer, ForeignKey("tb_correntista.cod_correntista"))
    tipo_transacao = Column(CHAR)
    valor_movimentacao = Column(FLOAT)
    data_operacao = Column(TIMESTAMP)
    chave_fk2 = relationship("Correntista", back_populates="chave_fk1")
