#desafio 1
"""
from datetime import date
anoAtual = date.today().year
diferenca = 2050 - anoAtual
idade = int(input("\nDigita tua idade : "))
print (f"Você nasceu em {anoAtual-idade} e Você vai ter {idade+diferenca} anos de idade")
""" 
#desafio 2
'''
nota = (input("\nDigite suas 3 notas : ").split(" "))
media = ((int(nota[0])+int(nota[1])+int(nota[2]))/3)
if (media > 0 and media < 3):
    print(f"\nReprovado com média {media}")
elif(media > 3 and media < 7):
    print(f"\nvai fazer o exame, tua média foi {media}")
elif(media > 7 and media <= 10):
    print(f"\nBoa, tua média foi {media}")
else:
    print("\nDigitasse algo errado ae")
'''
#desafio 3
'''
inicio = int(input("digite o primeiro numero : "))
fim = int(input("digite o segundo numero : "))

if(inicio < fim):
    inicio = inicio + 1 
    while(inicio < fim):
        print("numero atual : ", inicio)
        inicio += 1
elif(fim < inicio):
    fim = fim + 1
    while(fim < inicio):
        print("numero atual : ", fim)
        fim += 1
'''
#desafio 4
'''
dataDigitada = input("Digite a data :")

meses = ["Janeiro", "Fevereiro", "Março", "Abril", 
        "Maio", "Junho", "Julho", "Agosto", 
        "Setembro", "Outubro", "Novembro", "Dezembro"]

lista = (dataDigitada.split("/"))
dia,mes,ano = int(lista[0]),int(lista[1]),(lista[2])
mesExtenso = meses[mes]

print("a data que você digitou foi", dia , "De" , mesExtenso, "Do ano ", ano )
'''