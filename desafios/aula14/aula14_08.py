r = "S"
cont = 0
soma = 0
maior = 0
menor = 0
while r == "S":
    n = int(input("Digite um número inteiro: "))
    r = str(input("Quer Continuar [S/N]: ")).upper()
    cont += 1

    if cont == 1:
        maior = n
        menor = n
    else:
        if n > maior:
            maior = n
        if n < menor:
            menor = n
    soma += n
media = soma / cont
print("A Média dos valores é = {:.2f}".format(media))
print("O Maior número é {}".format(maior),
      "\nO Menor número é {}".format(menor))