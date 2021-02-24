s = 0
v = 0
for c in range (1, 7):
    n = int(input("Digite o {}º número: ".format(c)))
    if n % 2 == 0:
        s += n
        v += 1
print("Tivemos {} ocorrências de números pares e sua soma é de {}".format(v, s))