r = "S"
somaProd = precoCount = cont = 0
while r == "S":
    print("-"*20, "CADASTRO DE PRODUTOS", "-"*20)
    nome = str(input("Nome: "))
    preco = float(input("Preço do produto: R$"))
    cont += 1

    somaProd += preco
    r = str(input("Quer continuar? [S/N] ")).upper()
    while r != "S" and r != "N":
        r = str(input("Quer continuar? [S/N] ")).upper()

    if preco > 1000:
        precoCount += 1

    if cont == 1:
        prodBat = preco
        nomeProd = nome
    else:
        if preco < prodBat:
            prodBat = preco
            nomeProd = nome

print("-"*10, "FIM DO PROGRAMA", "-"*10,
      f"\nTotal da compra: R${somaProd:.2f}",
      f"\nProdutos que custam mais de R$1000: {precoCount}",
      f"\nO produto mais barato é {nomeProd} custando R${prodBat:.2f}")
