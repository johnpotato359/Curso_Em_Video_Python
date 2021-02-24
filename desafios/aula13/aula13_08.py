import re
#Palíndromos

#Receber a Frase
frase = str(input("Digite uma frase ou palavra: "))

#Retirar os espaços
frase = re.sub(r"\s+", "",frase).upper()

#Inverte a String
print("O inverso de {} é {}".format(frase, frase[::-1]))

#Compara a String
if frase == frase[::-1]:
    print("A frase digitada é Palíndromo!")
else:
    print("A frase digitada Não é Palíndromo!")