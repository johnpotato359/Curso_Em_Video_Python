dado = []
pessoas = []
lista = []
while True:
    dado.append(str(input("Nome: ")))
    dado.append(int(input("Peso: ")))
    pessoas.append(dado[:])
    dado.clear()
    resp = " "
    resp = str(input("Quer Continuar?[S/N] ")).strip().upper()[0]
    if resp in "Nn":
        print("PROGRAMA ENCERRADO!")
        break

for p in pessoas:
    lista.append(p[1])
print(sorted(lista))
