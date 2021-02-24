sal = float(input("Digite o seu salário: R$"))
nSal = sal + (sal * 0.15)

print("O salário sem promoção: R${}".format(sal),
      "\nSalário com 15% de aumento após a promoção: R${:.3f}".format(nSal))