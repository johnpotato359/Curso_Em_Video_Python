cont = 1
while True:
    print(cont, '->', end="")
    cont += 1
    if cont >= 11:
        break
print("Acabou")

n = s = 0
while True:
    n = int(input("Digite um número: "))
    if n == 999:
        break
    s += n
print(f"A soma vale {s}")

# f strings

nome = "José"
idade = 44
salario = 987.35
print(f"O {nome} tem {idade} anos e ganha R${salario:.2f}")


