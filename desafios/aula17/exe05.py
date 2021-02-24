lista0 = []
lista_par = []
lista_impar = []
i = 0
while True:
    lista0.append(int(input(f"Digite N{i}: ")))
    if lista0[i] % 2 == 0:
        lista_par.append(lista0[i])
    else:
        lista_impar.append(lista0[i])
    i += 1
    resp = " "
    resp = str(input("Quer Continuar?[S/N] ")).strip().upper()[0]
    if "N" in resp:
        print(f"Lista: {lista0}",
              f"\nLista de números pares: {lista_par}",
              f"\nLista de números ímpares: {lista_impar}")
        break
