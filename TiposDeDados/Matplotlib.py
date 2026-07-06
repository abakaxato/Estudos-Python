#plotando o primeiro grafico
import matplotlib.pyplot as plt
import pandas as pd

'''
#colocar o ";" serve para ocultar as informações do objeto criado
    #sempre que plotar o primeiro valor vai ser considerado X e o segundo Y

plot1 = [2,5,10,15,24,56];
plot2 = [23,87,54,67,9,89];
plot3 = [26,36,45,69,40,91];
plot4 = [30,100,58,71,82,93];

#exibindo o plot em barra
plt.bar(plot1,plot2)

#exibindo o plot em grafico
plt.plot(plot1,plot2)

#formatando o estilo que vai ser exibido o grafico
plt.plot(plot1,plot2,'k-.x')

#um X e varios Y ( o X é repetido)
plt.plot(plot1,plot2,'ro-',plot1,plot3,'go-',plot1,plot4,'bo-')
#colocando um titulo
plt.title("Exemplo de varios X")
'''
#filtrando a tabela pelo Mês
tempo = pd.read_csv(r'ArquivosTeste\BeloHorizonte.csv')
x_periodo = tempo[tempo['Mes'] == 1]

# Criando um gráfico da temperatura ao longo do dia
plt.plot(x_periodo['Hora'], x_periodo['TBSC'], 'ro-')
plt.xlabel('Hora do Dia')
plt.ylabel('Temperatura (°C)')
plt.title('Temperatura em Belo Horizonte - Mês 1')
plt.show()