from fastapi import FastAPI
import mysql.connector

conectar = mysql.connector.connect(user='lucky', password='D@nidani1985',
                                   host='localhost', database='db_bancoSa',
                                   auth_plugin='mysql_native_password')
app = FastAPI()


@app.get("/")
def hello_root():
    return {"message": "Teste"}
