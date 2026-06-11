
#Uso de pandas

import pandas as pd

#Series é praticamente um vetor e você tem am opção de mudaros identificadores dos indíces

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
seriesComIndiceTxt = pd.Series([3,4,6,8,4,9], index = ['a','b','c','d','e','f'])
print('Serie sem com indice em texto:\n',seriesComIndiceTxt,'\n')



numero = input("Clice em enter...")