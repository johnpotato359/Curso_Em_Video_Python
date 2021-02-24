import random
r = random.randrange(0, 5)

print("O Computador Major Tom pensou em um número entre 0 e 5, tente adivinhá-lo!")
num = int(input("Digite um número INTEIRO entre 0 e 5: "))

if num == r:
    print("Parabéns, você acertou o número!!")
else:
    print("O número era {}, tente novamente.".format(r))

