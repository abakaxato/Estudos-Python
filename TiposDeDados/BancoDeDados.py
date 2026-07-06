import sqlite3 as sl
import pandas as pd
import matplotlib.pyplot as plot
'''
#se conectando a um banco de dados, caso não exista ele cria
conexao = sl.connect(r'ArquivosTeste\Pessoas.db')
#Criando um cursor para ser usado no banco de dados
cursor = conexao.cursor()
#Criando uma query que pode ser usada no cursor para manipular o banco
sql = r'CREATE TABLE pessoas (id INT AUTO_INCREMENT PRIMARY KEY,nome VARCHAR(100) NOT NULL,cpf VARCHAR(11) UNIQUE NOT NULL,data_nascimento DATE,email VARCHAR(100),data_cadastro TIMESTAMP DEFAULT CURRENT_TIMESTAMP)'
sql2 = r"INSERT INTO pessoas (nome, cpf, data_nascimento, email) VALUES ('João Silva', '12345678901', '1995-05-15', 'joao.silva@email.com');"
#Executando a query utilizando o cursor
cursor.execute(sql)
cursor.execute(sql2)

#Inserindo valores no banco de dados a partir de uma lista
sql3 = "INSERT INTO pessoas (nome, cpf, data_nascimento, email) VALUES (?,?,?,?)"
pessoas = (['joão','12234','1995-05-16','joao.silva@email.com'],['Maria','14234','1995-05-56','Maria.silva@email.com'],['Ravena','123544','1995-04-16','Ravena.silva@email.com'])
for pessoas in pessoas:
    cursor.execute(sql3,pessoas)
conexao.commit()

#Puxando os dados do banco de dados
sql4 = 'SELECT * FROM PESSOAS'
cursor.execute(sql4)
SqlSelect = cursor.fetchall()
    #Printando apenas um valor
print(SqlSelect)
    #Printando varios valores decorrendo da tabela
for pessoas in SqlSelect:
    print(pessoas)

print("\n\n\n")

#Puxando dados do banco utilizando filtros
sql5 = 'SELECT * FROM Pessoas WHERE CPF < 12345'
cursor.execute(sql5)
SqlSelect2 = cursor.fetchall()
print(SqlSelect2)
for pessoas in SqlSelect2:
    print(pessoas)

print("\n\n\n")

#Puxando dados individuais do banco
sql6 = 'SELECT * FROM Pessoas WHERE CPF < 12345'
cursor.execute(sql6)
SqlSelect3 = cursor.fetchall()
print(SqlSelect3)
for id, nome, cpf, data_nascimento, email, data_cadastro in SqlSelect3:
    print(nome,cpf,email)

#importando dados de um banco de dados para um data frame
df = pd.read_sql_query('SELECT * FROM PESSOAS',conexao)
print (df)

#importando dados de temperatura do banco de dados para um data frame
    #criação de conexão ou criação do banco
conexao2 = sl.connect(r'ArquivosTeste\BeloHorizonte.db')
    #Criação do cursor responsavel por manipular o banco
cursor2 = conexao2.cursor()
    #criação de data frame com os dados de uma tabela
pdTemperatura = pd.read_csv(r'ArquivosTeste\BeloHorizonte.csv')
    #tranformação do data frame criado em uma tabela na conexão escolhida(se existir é sobreposta)
pdTemperatura.to_sql('Temperatura',conexao2,if_exists='replace')
    #Executando um select utilizando o cursor criado na conexao correta
cursor2.execute('SELECT * FROM Temperatura LIMIT 10')
    #Associando o valor que foi retornado no cursor a uma variavel
bdTemperatura = cursor2.fetchall()
    #Imprimindo as linhas contidas dentro da variavel

for temperaturas in bdTemperatura:
    print(temperaturas)

#Imprimindo os valores que existem no banco utilizando pandas e gerando grafico
exibicao = pd.read_sql_query('Select * from Temperatura LIMIT 10',conexao2)
exibicao.plot(kind='bar')
plot.show()
'''