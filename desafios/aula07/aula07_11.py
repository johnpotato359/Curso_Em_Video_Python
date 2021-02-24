km = float(input("Digite a quantidade de KM percorridos: "))
DiasAlugados = int(input("Quantidade de dias Alugados: "))
CustoAluguel = (60 * DiasAlugados) + (0.15 * km)

print("O Aluguel do Carro ficará R${:.2f}".format(CustoAluguel))