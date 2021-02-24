r = "S"
countId = countHm = countMh = 0

while r == "S":
    print("-"*20,
          "\nCADASTRE UMA PESSOA")
    print("-"*20)
    idade = int(input("Idade: "))
    sexo = str(input("Sexo: [M/F] ")).upper()
    while sexo != "M" and sexo != "F":
        sexo = str(input("Sexo: [M/F] ")).upper()
    r = str(input("Quer continuar? [S/N] ")).upper()
    while r != "S" and r != "N":
        r = str(input("Quer continuar? [S/N] ")).upper()

    if idade > 18:
        countId += 1
    if sexo == "M":
        countHm += 1
    if sexo == "F" and idade < 20:
        countMh += 1

print("="*6, "FIM DO PROGRAMA", "="*6)
print(f"Pessoas que tem mais de 18 anos: {countId}",
      f"\nHomens que foram cadastrados: {countHm}",
      f"\nMulheres que tem menos de 20 anos: {countMh}")
