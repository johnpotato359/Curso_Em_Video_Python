frase = input("Digite o seu Nome: ").strip()
lista = frase.split()
#Todas as letras Maiúsculas
print("Seu nome em Maiúsculas é {}"
      .format(frase.upper()))

#Todas as letras Minúsculas
print("Seu nome em Minúsculas é {}"
      .format(frase.lower()))

#Quantas letras sem considerar o espaço
print("Quantas letras ao todo: {}"
      .format(len(frase) - frase.count(" ")))

#Quantas letras tem o primeiro nome
print("Seu primeiro nome é {} e ele tem {} letras"
      .format(lista[0], len(lista[0])))

