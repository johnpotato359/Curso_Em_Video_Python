somaProd = precoCount = count = 0
while True:
    print("-" * 20, "CADASTRO DE PRODUTOS", "-" * 20)
    nome = str(input("Nome: "))
    preco = float(input("Preço do produto: R$"))
    count += 1
    somaProd += preco

    resp = " "
    while resp not in "SN":
        resp = str(input("Quer continuar? [S/N] ")).strip().upper()[0]
    if resp in "N":
        break

    if preco > 1000:
        precoCount += 1

    if count == 1:
        prodBat = preco
        nomeProd = nome
    else:
        if preco < prodBat:
            prodBat = preco
            nomeProd = nome

print("-" * 20, "FIM DO PROGRAMA", "-" * 20)
print(f"Total da compra: R${somaProd:.2f}",
      f"\nProdutos que custam mais de R$1000: {precoCount}",
      f"\nO produto mais barato é {nomeProd} custando R${prodBat:.2f}")
