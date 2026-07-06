#plotando o primeiro grafico
import matplotlib.pyplot as plt

#colocar o ";" serve para ocultar as informações do objeto criado
plot1 = [2,5,10,15,24,56];
plot2 = [23,34,54,67,78,89];

#exibindo o plot em barra
#plt.bar(plot1,plot2)

#exibindo o plot em grafico
#plt.plot(plot1,plot2)

#formatando o estilo que vai ser exibido o grafico
plt.plot(plot1,plot2,'k-.x')


plt.show()