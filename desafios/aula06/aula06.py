n1 = int(input("Digite um valor "))
n2 = float(input("Digite um valor "))
s = n1 + n2
print("O valor entre {} e {} é = {}".format(n1, n2, s))
print(type(s))

q = input("Digite qualquer coisa ")
print("O dado é caractere: {}".format(q.isalpha()))

q = input("Digite qualquer coisa ")
print("O dado é numérico: {}".format(q.isnumeric()))
