from random import randint
from time import sleep

numPc = randint(0,10)
palpites = 0
acertou = False
print("O Computador Major Tom está pensando em um número entre 0 e 10")
sleep(2)
print("Pensando...")
sleep(3)
print("Só mais um pouquinho...")
sleep(2)

n = int(input("Major Tom pensou em um número! Tente advinhá-lo: "))
print(numPc)

while not acertou:
    if n < numPc:
        print("Mais... Tente mais uma vez.")
    else:
        print("Menos... Tente mais uma vez.")
    n = int(input("Qual o seu palpite: "))
    palpites += 1
    if n == numPc:
        palpites += 1
        acertou = True
print("Parabéns você acertou o número! Ao todo foram {} palpite(s).".format(palpites))