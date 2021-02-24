peso = float(input("Digite o seu peso em KG: "))
altura = float(input("Digite a sua altura em m: "))
imc = peso / (altura * altura)

print("O seu IMC é de {:.1f}".format(imc), end=". ")
if imc < 18.5:
    print("Você está Abaixo do Peso")
elif imc >= 18.5 and imc <=25:
    print("Você está no Peso Ideal")
elif imc > 25 and imc <= 30:
    print("Você está com Sobrepeso")
elif imc > 30 and imc <= 40:
    print("Você está com Obesidade")
else:
    print("CUIDADO!! Obesidade Mórbida")
