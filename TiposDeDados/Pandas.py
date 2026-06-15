
#Uso de pandas

import pandas as pd
import matplotlib.pyplot as plt
'''
#Series é praticamente um vetor e você tem varias opções de como manipular ele de forma mais flexivel

# Quando você não escolhe o indice ele é criado de forma normal inteira a partir de 0.
seriesSemIndice = pd.Series([3,4,6,8,4,9])
print('\n Serie com indice automatico:\n',seriesSemIndice,'\n')

# Você pode colocar de forma manual os indices após a declaração dos valores
seriesComIndice = pd.Series([3,4,6,8,4,9], index = [6,3,1,4,2,5])
print('Serie sem com indice númerico manual:\n',seriesComIndice,'\n')

#Você pode também usar textos para identificar os indices.
seriesComIndiceTxt = pd.Series([3,4,6,8,4,9], index = ['a','b','c','d','e','f'])
print('Serie sem com indice em texto:\n',seriesComIndiceTxt,'\n')

#é possivel colocar valores diretamente dentro da serie atraves de um dicionario.
funcionarios = {'joão': 1500, 'Maria':900,'Jose':50}
seriesFuncionarios = pd.Series(funcionarios)
print('Serie de funcionarios:\n',seriesFuncionarios,'\n')

#Também é possivel usar algumas funções com as series

 #Ordenando pelo index (antes tava toda bagunçada), precisa do "inplace= True" para editar o objeto...
seriesComIndice.sort_index( inplace= True)
print('ordenada por indice\n',seriesComIndice)

 #Ordenando pelos valores, precisa do "inplace= True" para editar o objeto...
seriesComIndice.sort_values( inplace= True)
print('ordenada por Valor\n',seriesComIndice)

#DataFrame é uma tabela em python (praticamente isso)

#Criando o dicionario que vai servir para o dataframe, o indentificador vira a coluna e indice é automatico
dados = {
    'Nome': ['Ana', 'Bruno', 'Carlos'],
    'Idade': [25, 30, 22],
    'Cidade': ['Recife', 'São Paulo', 'Rio de Janeiro']
}
print("\n",dados)

#DataFrame sendo criado a partir de um dicionario.
df = pd.DataFrame(dados)
print("\n",df,"\n")
#limitando o numero de registros exibidos pegando apoenas o primeiro.
print(df.head(1),"\n")
#limitando o numero de registros exibidos pegando apoenas o ultimo.
print(df.tail(1),'\n')
#limitando o numero de registros exibidos pegando apoenas um dado aleatorio.
print(df.sample(1))
#usando um método para descrever algumas caracteristicas da "tabela
print(df.describe())
#lendo um arquivo.csv e importando para o dataframe
arquivoCsv = pd.read_csv('ArquivosTeste/TestePython.csv',sep=';')
print(arquivoCsv)
#Adicionando uma nova coluna no dataFrame
arquivoCsv['Ativa'] = 'Não'
print(arquivoCsv)
#limitando o numero de colunas no dataFrame
arquivoCsv2 = pd.read_csv('ArquivosTeste/TestePython.csv',sep=';',usecols=[1,2])
print(arquivoCsv2)
#renomeando colunas no data Frame
arquivoCsv3 = pd.read_csv('ArquivosTeste/TestePython.csv',sep=';',names=["coluna1","coluna2","coluna3"])
print(arquivoCsv3)
#Removendo linhas duplicadas do dataFrama
arquivoCsv4 = pd.read_csv('ArquivosTeste/TestePython.csv',sep=';')
arquivoCsv4.drop_duplicates()
print(arquivoCsv4)
#filtrando as colunas do dataFrame
arquivoCsv5 = pd.read_csv('ArquivosTeste/TestePython.csv',sep=';')
print(arquivoCsv5[(arquivoCsv5.Idade>23)])
#somando filtros
print(arquivoCsv5[(arquivoCsv5.Idade > 23) & (arquivoCsv5.Idade < 55 )])
#utilizando o método query
print(arquivoCsv5.query('Idade <= 33 or Idade > 55'))
#contando repetições de dados de uma coluna
arquivoCsv6 = pd.read_csv('ArquivosTeste/TestePython.csv',sep=';')
print(arquivoCsv6.Idade.value_counts())

#Criando um novo arquivo csv a partir do python
arquivoCsv6 = pd.read_csv('ArquivosTeste/TestePython.csv',sep=';')
arquivoCriado = arquivoCsv6[(arquivoCsv6.Idade > 23) & (arquivoCsv6.Idade < 55)]
arquivoCriado.to_csv(ArquivosTeste/saida.csv', index=False, sep=';')

#Gerando um grafico a partir de um arquivo csv
arquivoCsv7 = pd.read_csv('ArquivosTeste/TestePython.csv',sep=';')
ax = arquivoCsv7.Idade.plot()
ax.set_xlabel('Linha')
ax.set_ylabel('Idade')
plt.show()

'''