#importando a biblioteca de conexão com o banco de dados com mysql
#vamos adicionar as ciclioteca

import  mysql.connector as mc

#vamos estabelecer a conexao com o banco de dados
#e para tal , iremos passar os seguintes dados 
#servidor porta usuario senha banco

conexao = mc.connect(
host="127.0.0.1",
port="3784",
user="root",
password="senac@123",
database="banco"
)

#print(conexao)

#para se m

cursor = conexao.cursor()
#cursor.execute("'cleber matrial ','cl@gmail.com','(11)378492'")

#cursor.execute("Create database Ola")
cursor.execute("Select * from banco.clientes")
print(cursor)
for c in cursor:
    print(f"id do cliente:{c[0]}"c)
    print(f"nome do cliente:{c[1]}"c)
    print(f"email do cliente:{c[2]}"c)