vCasa = float(input("Digite o valor da casa: R$"))
vSal = float(input("Digite o seu salário: R$"))
qtdAno = int(input("Digite em quantos anos de financiamento: "))

prestacao = vCasa // (qtdAno * 12)

if prestacao > (vSal*0.3):
    print("Para pegar uma casa de R${:.2f} em {} anos "
          "a prestação será de R${:.2f}".format(vCasa, qtdAno, prestacao))
    print("EMPRÉSTIMO NEGADO!")
else:
    print("Para pegar uma casa de R${:.2f} em {} anos "
          "a prestação será de R${:.2f}".format(vCasa, qtdAno, prestacao))
    print("Parabéns, o seu EMPRÉSTIMO ESTÁ APROVADO!")