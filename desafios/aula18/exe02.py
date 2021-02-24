valores = []
dado = []

for i in range(0, 7):
    dado.append(int(input(f"Digite o {i+1}º valor: ")))
    valores.append(dado[:])
    dado.clear()

for p in valores:
    print(p)
