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