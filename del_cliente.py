import mysql.connector as mc
import os
con = mc.connect(
    host="127.0.0.1",
    port="3784",
    user="root",
    password="senac@123",
    database="banco"
)

cursor = con.cursor()
cursor.execute("select * from clientes")
for c in cursor:
    print(c)

id = input("Digite o id que você deseja apagar: ")
rs =input("para escluir coloque S para não N: ")
if(rs =="s" or rs =="S"):
    cursor.execute("delete from clientes where cliente_id"+id)
    con.commit
else:
    print("------------ obrigado por acessar sistema ------------")