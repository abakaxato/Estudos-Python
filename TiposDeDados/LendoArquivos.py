#Escrevendo em arquivos.txt
    #Se o arquivo não existir ele é criado
    #como eu coloquei "w" o arquivo vai ser sobrescrito
arquivo = open(r"arquivosTeste\entrada.txt","w")
#arquivo.write("Esse-texto-foi-sobrescrito")
arquivo.close
#com o "a" o texto é adicionado
arquivoAppend = open(r"arquivosTeste\entrada.txt","a")
arquivoAppend.write("\nEsse-texto-foi-adicionado-depois")