vel = int(input("Digite a velocidade do carro: "))
multa = (vel - 80) * 7
if vel > 80:
    print("Você ultrapassou o limite de velocidade e será MULTADO!")
    print("A sua multa foi de R${:.2f}".format(multa))
else:
    print("Você está dentro do limite de velocidade, Parabéns!")