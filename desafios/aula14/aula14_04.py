print("="*10, "Cálculo Fatorial", "="*10)
f = int(input("Digite um NÚMERO INTEIRO: "))
c = 1
while f != 0:
    print("{} ".format(f), end="")
    print(" x " if f > 1 else " = ", end="")
    c = c * f
    f -= 1''
print(c)