n = int(input("Digite um número para a tabuada: "))
print("=" * 15)
for c in range(1, 11):
    print("{} X {} = {}".format(n, c, n*c))

