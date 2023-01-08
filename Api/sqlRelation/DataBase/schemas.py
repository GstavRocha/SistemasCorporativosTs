from typing import List, Any

from datetime import datetime
import peewee
from pydantic import BaseModel
from pydantic.utils import GetterDict

class PeeweeGetterDict(GetterDict):
    def get(self,key: Any, default: Any = None):
        res  = getattr(self._obj, key, default)
        if isinstance(res, peewee.ModelSelect):
            return list(res)

class Correntista_Schema(BaseModel): #aqui ele não restorna
    cod_correntista: int
    nome_correntista: str
    email_correntista: str
    saldo_correntista: float

class getCorrentista(Correntista_Schema):
    cod_correntista: int
    class Config:
        orm_mode = True
class createUser(Correntista_Schema):
    cod_correntista: int
    nome_correntista: str
    email_correntista: str
    saldo_correntista: float
    class Config:
        orm_mode= True

class putUser(Correntista_Schema):
    nome_correntista: str
    email_correntista: str
    class Config:
        orm_mode= True
class Movimentacao_Schema(BaseModel):
    cod_movimentacao: int
    cod_correntista: int
    tipo_transacao: str
    valor_movimentacao: float
    data_operacao: datetime
class Correntista_nome(Correntista_Schema):
    cod_correntista: int
    nome_correntista: str
    class Config:
        orm_mode = True
class getMovimetancoes(Movimentacao_Schema):
    cod_movimentacao: int
    cod_correntista: int
    tipo_transacao: str
    valor_movimentacao: float
    class Config:
        orm_mode= True
class getMovimentacao(Movimentacao_Schema):
    cod_movimentacao: int
    class Config:
        orm_mode=True
