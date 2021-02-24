distViag = float(input("Digite a distância da viagem em KM: "))

if distViag <= 200:
    preco = 0.5 * distViag
    print("Você viajará {:.1f}Km e pagará R${:.2f}".format(distViag, preco))
else:
    preco = 0.45 * distViag
    print("Você viajará {:.1f}Km e pagará R${:.2f}".format(distViag, preco))