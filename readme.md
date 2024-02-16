# Conexão do python com mysql
<center><img src="https://miro.medium.com/v2/resize:fit:1137/1*OnDVcS17HTWZ2L2vPaaQ1A.png" height="500" width="700"></center>


## driver de comunicação
para estabelecer a comunicação entre o python e o
banco de dados de dados mysql, iremos 
usar o seguinte drive:
<a href="></a>

### comando para instalar o  driver

```   python
    python -m pip install mysql-connector-python

```

###configuração do banco de dados mysql
O nosso banco de dados está um conteiner de cocker. Para acessá-lo será nessesario criar o conteiner, ent~eo seguintes comandos em um servidor fedora com docker instalado:

### criação de volume
```shell
mkidir dadosclientes
```

#### criação do conteiner
<center><img src="https://cdn.iconscout.com/icon/free/png-256/free-social-275-116309.png?f=webp" height="100" width="100"></center>

```
 docker run --name  srv-mysql -v ~/dadosclientes:/var/lib/mysql -p 3784:3306 -e  MYSQL_ROOT_PASSWORD=senac@123 -d mysql
```
### criação de banco de dados e  tabela crientes
```sql
create database banco;
use banco;
create table clientes(
 cliente_id int auto_increment primary key,
nome_cliente varchar(50) not null,
email varchar(100) not null unique,
telefone varchar(20) not null unique
);
```

### arquivos clientes
```
# importando a biblioteca de conexão com o banco
# de dados mysql
# vamos adicionar um alias a biblioteca
import mysql.connector as mc

# Vamos estabelecer a conexao com o banco
# de dados e para tal, iremos passar os 
# seguintes dados:
# servidor, porta, usuario, senha, banco
conexao = mc.connect(
    host="127.0.0.1",
    port="3784",
    user="root",
    password="senac@123",
    database="banco"
)
# Estamos testando a conexão, pedindo para 
# exibir o id da conexão. Caso exiba uma 
# pilha de erros, então você tem um erro
# na linha de conexão
print(conexao)

#para se movimentar dentro da estrutura de 
# banco de dados e retornar dos dados necessários
# iremos criar um cursor
cursor = conexao.cursor()

# Vamos executar um comando usando o cursor
# cursor.execute("Create database Ola")

# cursor.execute("insert into clientes(nome_cliente,email,telefone)values('Amanda','amanda@uol.com.br','(54) 9985-6854')")

# Vamos selecionar todos dados da tabela clientes
cursor.execute("Select * from banco.clientes")
print(cursor)
for c in cursor:
    print(f"Id do Cliente: {c[0]}")
    print(f"Nome do Cliente: {c[1]}")
    print(f"E-Mail: {c[2]}")

```
## adição pelo usuario
```
import mysql.connector as mc

# estabelecer a conexao com o banco
cx = mc.connect(
    host="127.0.0.1",
    port="3784",
    user="root",
    password="senac@123",
    database="banco"
)
# verificar se a conexao foi estabelecida
print(cx)

# Criação de variáveis para o usuário passar os dados do cliente
# para cadastrar
nome = input("Digite o nome do cliente: ")
email = input("Digite o email do cliente: ")
telefone = input("Digite o telefone do cliente: ")

cursor = cx.cursor()
cursor.execute("insert into clientes(nome_cliente,email,telefone)values('"+nome+"','"+email+"','"+telefone+"')")
# confirmar a inserção dos dados na tabela
print(cx.commit())


```
### arquivo de update
```
import mysql.connector as mc

cx = mc.connect(
    host="127.0.0.1",
    port="3784",
    user="root",
    password="senac@123",
    database="banco"
)

cursor = cx.cursor()
cursor.execute("Select * from clientes")
for i in cursor:
    print(i)
print("------------------------------------------------")
print("O você deseja atualizar , digite: ")
print("1 - para Nome")
print("2 - para E-mail")
print("3 - para Telefone")
op = input ("Digite a opção desejada: ")
id = input("Agora digite o id do cliente:")
dado = input("Digite a nova informação: ")
if(op == "1"):
    cursor.execute("update clientes set nome_cliente='"+dado+"' where cliente_id="+id)
elif(op == "2" ):  
     cursor.execute("update clientes set email='"+dado+"' where cliente_id="+id)
elif(op =="3"):
        cursor.execute("update clientes set telefone='"+dado+"' where cliente_id="+id)
else:
     print("Opção invalida :( ")

cx.commit()
```