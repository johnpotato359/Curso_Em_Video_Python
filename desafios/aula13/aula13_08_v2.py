frase = str(input("Digite uma frase: ")).strip().upper().split()
junto = "".join(frase)
inver = ''

for i in range(len(junto) - 1, -1, -1):
    inver += junto[i]

if (junto == inver):
    print("A frase ou palavra digitada É UM PALÍNDROMO")
else:
    print("A frase ou palavra digitada NÃO É UM PALÍNDROMO")

print("Você digitou a frase ou palavra {} o inverso é {}".format(junto, inver))