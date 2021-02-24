n1 = float(input("Digite a sua nota N1: "))
n2 = float(input("Digite a sua nota N2: "))
media = (n1 + n2) / 2

if media < 5.0:
    print("REPROVADO!")
elif media >= 5.0 and media <= 6.9:
    print("RECUPERAÇÃO")
else:
    print("APROVADO")
