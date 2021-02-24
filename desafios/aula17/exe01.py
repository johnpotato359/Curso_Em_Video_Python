valores = []
maior = []
menor = []
for i in range(0, 5):
    valores.append(int(input(f"Digite N{i}: ")))
print("=-" * 30)
for c, v in enumerate(valores):
    if v == max(valores):
        maior.append(c)
        # print(c, end="... ")
    if v == min(valores):
        menor.append(c)
        # print(c, end="... ")
print(f"Você digitou os valores {valores}")
print(f"Maior Número é {max(valores)} nas posições ", maior)
print(f"Menor Número é {min(valores)} nas posições ", menor)
# print(f"Maior Número é {max(valores)} e sua posição é {valores.index(max(valores))}",
#       f"\nMenor Número é {min(valores)} e sua posição é {valores.index(min(valores))}")
