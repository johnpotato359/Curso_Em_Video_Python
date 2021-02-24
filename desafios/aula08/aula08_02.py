import math

cO = float(input("Digite o comprimento do CATETO OPOSTO de um TRIÂNGULO RETÂNGULO: "))
cA = float(input("Digite o comprimento do CATETO ADJACENTE de um TRIÂNGULO RETÂNGULO: "))

print("O comprimento da HIPOTENUSA é = {:.2f}".format(math.hypot(cO, cA)))