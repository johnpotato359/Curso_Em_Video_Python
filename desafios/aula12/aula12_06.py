anoNasc = int(input("Digite o seu ANO de NASCIMENTO: "))

if anoNasc <= 9:
    print("Categoria MIRIM")
elif anoNasc <= 14:
    print("Categoria INFANTIL")
elif anoNasc <= 19:
    print("Categoria JUNIOR")
elif anoNasc == 20:
    print("Categoria SÊNIOR")
else:
    print("Categoria MASTER")