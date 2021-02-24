#Contagem de forma crescente até 5 vezes
print("Contagem Crescente")
for c in range (0,6):
    print(c)

print("==========")
#Contagem de forma regressivamente
print("Contagem Regressiva")
for c in range (6, 0, -1):
    print(c)

#Contagem crescente de 2 em 2
print("Contagem Crescente de 2 em 2")
for c in range (0, 6, 2):
    print(c)

#O f+1 é para a contagem realemente parar no número desejado
i = int(input("Início: "))
f = int(input("Fim: "))
p = int(input("Passo: "))
for c in range(i, f+1, p):
    print(c)
print("FIM")

#Somatório
s = 0
for c in range(0,4):
    n = int(input("Digite um número: "))
    s += n
print("A soma é {}".format(s))

