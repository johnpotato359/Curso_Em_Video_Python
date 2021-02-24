n = 1
cont = 0
soma = 0
while n != 0:
    n = int(input("Digite um número: "))
    if n == 999:
        n = 0
        cont -= 1
    cont += 1
    soma += n
print("Ao todo foram digitados {} números".format(cont),
      "\nA soma dos números digitados é = {}".format(soma))