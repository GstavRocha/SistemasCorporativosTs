from typing import List
import peewee
from pydantic import BaseModel

class PeeweeGet(GetterDict):
#https://fastapi.tiangolo.com/pt/advanced/sql-databases-peewee/?h=schemas#create-a-peeweegetterdict-for-the-pydantic-models-schemas