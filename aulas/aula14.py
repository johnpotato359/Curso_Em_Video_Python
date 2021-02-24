#for c in range(1, 10):
#    print(c)
#print("Fim")

#Exemplo de contagem com While
c = 1
while c < 10:
    print(c)
    c += 1
print("Fim")

#Exemplo While com condição de parada
r = "S"
while r == "S":
    n = int(input("Digite um valor: "))
    r = str(input("Quer continuar? [S/N] ")).upper()
print("Fim")

#Exemplo02
m = 1
par = impar = 0
while m != 0:
    m = int(input("Digite um valor: "))
    if m != 0:
        if m % 2 == 0:
            par += 1
        else:
            impar += 1
print("Você digitou {} números pares "
      "e {} números ímpares.".format(par, impar))

