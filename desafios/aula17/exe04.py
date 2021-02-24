valores = []
i = 0
while True:
    valores.append(int(input(f"Digite N{i}: ")))
    i += 1
    resp = " "
    resp = str(input("Quer Continuar?[S/N] ")).strip().upper()
    if "N" in resp:
        break
print(f"Ao todo foram {len(valores)} números inseridos na lista")

for j in range(0, len(valores)):
    for i in range(len(valores)-1, 0, -1):
        if valores[i] > valores[i - 1]:
            aux = valores[i]
            valores[i] = valores[i - 1]
            valores[i - 1] = aux
print(f"Lista decrescente: {valores}")
print(f"O Valor 5 FAZ parte da lista e está na posição {valores.index(5)}"
      if 5 in valores else "O valor 5 NÃO FAZ parte da lista")
