#Escrevendo em arquivos.txt
    #Se o arquivo não existir ele é criado
    #como eu coloquei "w" o arquivo vai ser sobrescrito
'''
arquivo = open(r"arquivosTeste\entrada.txt","w")
arquivo.write("Esse-texto-foi-sobrescrito")
arquivo.close
#com o "a" o texto é adicionado
arquivoAppend = open(r"arquivosTeste\entrada.txt","a")
arquivoAppend.write("\nEsse-texto-foi-adicionado-depois-2")
#Lendo os dados de um arquivo linha a linha
    #com o "r" o texto é lido
arquivoLeitura = open(r"arquivosTeste\entrada.txt","r")
for linha in arquivoLeitura:
    print(linha)
'''
#Lendo os dados de um arquivo palavra por palavra
    #com o "r" o texto é lido
arquivoLeituraPal = open(r"arquivosTeste\entrada.txt","r")
i = 1
for linha in arquivoLeituraPal:
    i = i + 1
    print(f"linha {i} :")
    print(linha.split("-"))
