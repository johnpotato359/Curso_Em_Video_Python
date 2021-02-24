media = 0.0
maior = 0
mNome = ""
qtdIdade = 0
for i in range(1, 5):
    nome = str(input("Digite o nome da {}º pessoa: "
                     .format(i)))
    idade = int(input("Digite a idade da {}º pessoa: "
                      .format(i)))
    sexo = str(input("Digite o sexo da {}º pessoa: "
                     .format(i))).upper()
    media += idade

    if i == 1 and sexo == "MASCULINO":
        maior = idade
        mNome = nome
    if idade > maior and sexo == "MASCULINO":
            mNome = nome


    if idade < 20 and sexo == "FEMININO":
            qtdIdade += 1

print("A média de idade do grupo é: {}".format(media/4))
print("O homem mais velho se chama {} e tem {} anos".format(mNome, maior))
print("A quantidade de mulheres com menos de 20 anos é {}"
      .format(qtdIdade))