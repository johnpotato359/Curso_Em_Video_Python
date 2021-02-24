sexo = str(input("Digite o sexo [M/F]: ")).strip().upper()[0]
while sexo not in "MmFf":
    sexo = str(input("Digite CORRETAMENTE [M/F]: ")).upper()
print("Dado {} computado com Sucesso".format(sexo))
