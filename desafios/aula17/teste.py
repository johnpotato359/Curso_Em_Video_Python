valores = []
i = 0
while True:
    valores.insert(int(input(f"N{i}: ")), i)
    i += 1
    resp = " "
    resp = str(input("Quer continuar?[S/N] ")).strip().upper()[0]
    if resp == "N":
        print(valores)
        break

