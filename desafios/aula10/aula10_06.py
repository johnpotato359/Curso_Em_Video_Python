n1 = int(input("Digite um número qualquer: "))
n2 = int(input("Digite um número qualquer: "))
n3 = int(input("Digite um número qualquer: "))
maior = n1
menor = n2

if n2 > n1 and n2 > n3:
    maior = n2
if n3 > n1 and n3 > n2:
    maior = n3
if n1 < n2 and n1 < n3:
    menor = n1
if n3 < n2 and n3 < n1:
    menor = n3
print("O maior número é {}".format(maior))
print("O menor número é {}".format(menor))