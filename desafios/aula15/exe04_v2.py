maisdezoito = cadH = mMenosvinte = 0
while True:
    print("-" * 10, "CADASTRO DE PESSOA", "-" * 10)
    idade = int(input("Idade: "))
    if idade >= 18:
        maisdezoito += 1
    sexo = " "
    while sexo not in "MF":
        sexo = str(input("Digite o sexo [M/F] ")).strip().upper()[0]
    if sexo in "M":
        cadH += 1
    resp = " "
    if sexo in "F" and idade < 20:
        mMenosvinte += 1
    while resp not in "SN":
        resp = str(input("Quer continuar? [S/N] ")).strip().upper()[0]
    if resp in "N":
        break
print("-" * 10, "DADOS REGISTRADOS", "-" * 10)
print(f"Pessoas maiores de 18 anos: {maisdezoito}",
      f"\nTotal de homens cadastrados: {cadH}",
      f"\nTotal de mulheres com menos de 20 anos: {mMenosvinte}")
