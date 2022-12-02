from typing import List
from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()


class Person(BaseModel):
    id: int
    name: str
    age: int


DB: List[Person] = [
    Person(id=1, name='Gustavo', age=37),
    Person(id=2, name='Dany', age=33),
    Person(id=3, name='Lucky', age=9)

]


@app.get("/api")
def read_root():
    return DB

