sal = float(input("Digite o seu salário: R$"))

if sal > 1250:
    sal += (sal*0.1)
    print("O seu aumento foi de 10% e ganhará R${:.2f}".format(sal))
else:
    sal += (sal * 0.15)
    print("O seu aumento foi de 15% e ganhará R${:.2f}".format(sal))
