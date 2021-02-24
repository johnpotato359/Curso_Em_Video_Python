from datetime import datetime
ano = 0
maioridade = 0
menoridade = 0
for i in range(1, 8):
    ano = int(input("Digite o ano de nascimento da pessoa {}º: "
                    .format(i)))
    if (datetime.today().year - ano >= 18):
        maioridade += 1
    else:
        menoridade += 1

print("O total de pessoas de MAIORIDADE é {}".format(maioridade),
      "\nO total de pessoas de MENORIDADE é {}".format(menoridade))

