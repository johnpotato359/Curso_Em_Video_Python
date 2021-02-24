precoCompras = float(input("Preço das Compras: R$"))
print("[ 1 ] à vista dinheiro/cheque ",
      "\n[ 2 ] à vista cartão ",
      "\n[ 3 ] 2x no cartão",
      "\n[ 4 ] 3x ou mais no cartão")
formaPag = int(input("Qual é a opção? "))
if formaPag == 1:
    val = precoCompras - (precoCompras * 0.1)
    print("Sua compra de R${:.2f} vai custar R${:.2f} no final"
          .format(precoCompras, val))

elif formaPag == 2:
    val = precoCompras - (precoCompras * 0.05)
    print("Sua compra de R${:.2f} vai custar R${:.2f} no final"
          .format(precoCompras, val))

elif formaPag == 3:
    val = precoCompras
    valParcela = val / 2
    print("Sua compra será parcelada em 2x de R${:.2f}"
          .format(valParcela))
    print("Sua compra de R${:.2f} vai custar R${:.2f} no final"
          .format(precoCompras, val))

elif formaPag == 4:
    parcelas = int(input("Quantas Parcelas? "))
    val = precoCompras + (precoCompras * 0.2)
    valParcela = val / parcelas
    print("Sua compra será parcelada em {}x de R${:.2f} COM JUROS"
          .format(parcelas, valParcela))
    print("Sua compra de R${:.2f} vai custar R${:.2f} no final"
          .format(precoCompras, val))
else:
    print("Reinicie o programa e digite um valor VÁLIDO!!")