#desafio 1
from datetime import date
anoAtual = date.today().year
diferenca = 2050 - anoAtual
idade = int(input("\nDigita tua idade : "))
print (f"Você nasceu em {anoAtual-idade} e Você vai ter {idade+diferenca} anos de idade")