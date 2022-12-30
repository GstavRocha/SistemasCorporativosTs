from typing import List, Any
import peewee
from pydantic import BaseModel
from pydantic.utils import GetterDict

# class PeeweeGetterDict(GetterDict):
#     def get(self,key: Any, default: Any = None):
#         res  = getattr(self._obj, key, default)
#         if isinstance(res, peewee.ModelSelect):
#             return list(res)

class Correntista_Schema(BaseModel): #aqui ele não restorna
    cod_correntista: int
    nome_correntista: str
    email_correntista: str
    saldo_correntista: float

class Correntista_nome(Correntista_Schema):
    cod_correntista: int
    nome_correntista: str
    class Config:
        orm_mode = True
        
