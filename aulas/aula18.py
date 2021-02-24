# teste = []
# galera = []
#
# teste.append("Gustavo")
# teste.append(40)
#
# galera.append(teste[:])
#
# teste[0] = "Maria"
# teste[1] = 22
#
# galera.append(teste[:])
#
# print(galera)

galera = [["João", 19], ["Ana", 33], ["Joaquim", 13], ["Maria", 45]]
print(galera[2][1])
for p in galera:
    print(f"Nome: {p[0]}", f"\nIdade: {p[1]}")
    print("-" * 30)

malta = []
dado = []
totmai = totmen = 0
#Ler os dados e copiar para uma lista
for i in range(0, 3):
    dado.append(str(input("Nome: ")))
    dado.append(int(input("Idade: ")))
    malta.append(dado[:]) #para fazer uma cópia de dados
    dado.clear()
print(malta)

# Tratamento dos dados
for p in malta:
    if p[1] >= 21:
        print(f"{p[0]} é maior de idade.")
        totmai += 1
    else:
        print(f"{p[0]} é menor de idade.")
        totmen += 1
print(f"Temos {totmai} maiores e {totmen} menores de idade.")