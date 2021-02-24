import math
import random

a1 = input("Nome do Aluno 01: ")
a2 = input("Nome do ALuno 02: ")
a3 = input("Nome do Aluno 03: ")
a4 = input("Nome do ALuno 04: ")

lista = [a1, a2, a3, a4]

sorteio = random.choice(lista)
print("O Escolhido foi : {}".format(sorteio))
