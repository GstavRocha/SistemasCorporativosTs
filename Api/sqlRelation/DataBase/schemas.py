from typing import List
from pydantic import BaseModel


class Correntista_Schema(BaseModel):
    id: int
    nome: str
    email: str
    saldo: float


class Movimentacao_Schema(BaseModel):
    id: int
    cod: int
    tipo: str
    valor: float
    data: int
class Correntista(BaseModel):
    id: int
    nome: str


class Saldo(Correntista_Schema):
    id: int
    nome: str
    saldo: float

    class Config:
        orm_mode = True


class Transferencia(Movimentacao_Schema):
    id: int
    nome: str
    cod: int
    valor: float

    class Config:
        orm_mode = True


class Deposito(Movimentacao_Schema):
    id: int
    nome: str
    valor: float

    class Config:
        orm_mode = True
class listaUsuario(Correntista):
    id: int
    nome: str

    usuarios: list[Correntista_Schema] = []
    class Config:
        orm_mode = True