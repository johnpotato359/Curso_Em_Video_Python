valores = []
i = 0
while True:
    n = int(input(f"Digite N{i}: "))
    if n not in valores:
        valores.append(n)
    else:
        print("Valor duplicado! Não vou adicionar...")
    resp = " "
    resp = str(input("Quer Continuar?[S/N] ")).strip().upper()[0]
    if resp == "N":
        print("=-" * 30)
        break
print(f"Valores da Lista: {valores}",
      f"\nLista crescente: {sorted(valores)}")
