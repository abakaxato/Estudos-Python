import sqlite3 as sl

#se conectando a um banco de dados, caso não exista ele cria
conexao = sl.connect(r'C:\Users\cauak\Desktop\Teste.db')
#Criando um cursor para ser usado no banco de dados
cursor = conexao.cursor()
#Criando uma query que pode ser usada no cursor para manipular o banco
sql = r'CREATE TABLE pessoas (id INT AUTO_INCREMENT PRIMARY KEY,nome VARCHAR(100) NOT NULL,cpf VARCHAR(11) UNIQUE NOT NULL,data_nascimento DATE,email VARCHAR(100),data_cadastro TIMESTAMP DEFAULT CURRENT_TIMESTAMP)'
#Executando a query utilizando o cursor
cursor.execute(sql)