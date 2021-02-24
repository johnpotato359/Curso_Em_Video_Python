lista_num = []
for c in range(0, 5):
    lista_num.append(int(input(f"Digite um valor para a Posição {c}: ")))
print("=-" * 30)
print(f"Você digitou os valores {lista_num}")
print(f"O Maior Valor digitado foi {max(lista_num)} nas posições ", end="")
for i, v in enumerate(lista_num):
    if v == max(lista_num):
        print(f"{i}... ", end="")
print()
print(f"O Menor Valor digitado foi {min(lista_num)} nas posições ", end="")
for i, v in enumerate(lista_num):
    if v == min(lista_num):
        print(f"{i}... ", end="")
