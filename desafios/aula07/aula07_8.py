p = float(input("Digite o preço do Produto: R$"))
nPreco = p - (p*0.05)

print("O Produto com o Preço de R${:.2f} está com desconto de 5% sendo o novo PREÇO de R${:.2f}"
      .format(p,nPreco))