nPrime = int(input("Digite um número inteiro: "))
mult = 0

for i in range(2, nPrime):
    if (nPrime % i == 0):
        print("Múltiplo de {}".format(i))
        mult += 1
if(mult == 0):
    print("O Número é PRIMO")
else:
    print("O Número não é PRIMO")