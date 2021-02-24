valores = []
aux = 0
for i in range(0, 5):
    valores.append(int(input(f"Digite N{i}: ")))
for i in range(0, len(valores)):
    for j in range(0, len(valores)-1):
       if valores[j] > valores[j + 1]:
           aux = valores[j]
           valores[j] = valores[j + 1]
           valores[j + 1] = aux
print(valores)