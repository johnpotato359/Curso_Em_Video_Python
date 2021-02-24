from math import sqrt, floor
# num = int(input("Digite um número: "))
# raiz = sqrt(num)
# print("A raiz de {} é igual a {}".format(num, floor(raiz)))

import random

# O módulo Random irá gerar um número aleatório decimal
num = random.random()
print(num)

# randint para gerar um número aleatório de 1 até 10
num01 = random.randint(1, 10)
print(num01)

# Importanto o módulo da internet
import emoji

print(emoji.emojize("Olá, Mundo :sunglasses::earth_americas:", use_aliases=True))
