# Tuplas são imutáveis
lanche = ("Hamburguer", "Suco", "Pizza", "Pudim", "Sorvete", "Chocolate")

print(lanche[1:3])
print(lanche[-1])

# Imprime tupla reversa
print(lanche[::-1])

print(lanche[::2])

# FORMAS DE IMPRIMIR UMA TUPLA

# for i in range(0, len(lanche)):
#     print(lanche[i], i)

# for i in lanche:
#     print(i)

for pos, i in enumerate(lanche):
    print(i, pos)

print(sorted(lanche))

a = (2, 5, 4)
b = (5, 8, 1, 2)
print(a + b)

# Podemos apenas apagar a tupla inteira
del(a)
