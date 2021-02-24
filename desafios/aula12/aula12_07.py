r1 = float(input("Digite o segmento da Reta 1: "))
r2 = float(input("Digite o segmento da Reta 2: "))
r3 = float(input("Digite o segmento da Reta 3: "))

if r1 < r2 + r3 and r2 < r1 + r3 and r3 < r1 + r2:
    print("Pode formar um triângulo", end=" ")
    if r1 == r2 == r3:
        print("Equilátero")
    elif r1 == r2 or r1 == r3:
        print("Isósceles")
    else:
        print("Escaleno")
else:
    print("Não pode formar um triângulo")