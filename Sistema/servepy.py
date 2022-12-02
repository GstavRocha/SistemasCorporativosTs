import mysql.connector

conectar = mysql.connector.connect(
    user='lucky', password='D@nidani1985',
    host='localhost', database='db_bancoSa',
    auth_plugin='mysql_native_password'
)
cursor = conectar.cursor()
print(conectar)
# TESTE
nome_correntista = 'DAny'
email_correntista = 'teste@email.com'
saldo_correntista = 100.0
inserir = f'INSERT INTO tb_correntista(nome_correntista, email_correntista, saldo_correntista) VALUES("{nome_correntista}","{email_correntista}", {saldo_correntista})'
cursor.execute(inserir)
conectar.commit()
cursor.close()
conectar.close()

