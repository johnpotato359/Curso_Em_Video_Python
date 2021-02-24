num = [6, 2, 7, 9]
num.append(14)
print(num)
num.sort()
print(num)
num.sort(reverse=True)
print(num)
num.insert(2, 0)
print(num)
num.pop(2)
print(num)
print(f"Esta lista tem {len(num)} elementos")
num.insert(2, 6) #insere o elemento 4 no índíce 2 num.insert(índice, elemento)
if 4 in num:
    num.remove(4)
else:
    print("Não achei o número 4")

valores = []
valores.append(5)
valores.append(9)
valores.append(4)
for c, v in enumerate(valores):
    print(f"Na posição {c} encontrei o valore {v}!")
print("Cheguei ao final da lista")

# for i in range(0, 5):
#     valores.append(int(input("Digite um valor: ")))
# print(valores)

# Ligação de listas

a = [2, 3, 4, 7]
b = a
print("-" * 40)
print("{:^40}".format("LIGAÇÃO DE LISTAS"))
print("-" * 40)
print(f"Lista A: {a}")
print(f"Lista B: {b}")
print("-" * 40)
b[2] = 8
print(f"Lista A: {a}")
print(f"Lista B: {b}")

# Copiar lista sem ligação
print("-" * 40)
print("{:^40}".format("COPIAR LISTA"))
print("-" * 40)
a = [2, 3, 4, 7]
b = a[:]
print(f"Lista A: {a}")
print(f"Lista B: {b}")

