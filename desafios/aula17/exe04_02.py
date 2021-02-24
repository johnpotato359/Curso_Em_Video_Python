valores = []
while True:
    valores.append(int(input("Digite um valor: ")))
    resp = str(input("Quer continuar?[S/N] ")).strip().upper()[0]
    if resp in "N":
        break
print("-=" * 30)
print(f"Você digitou {len(valores)} elementos")
valores.sort(reverse=True)
print(f"Lista Decrescente: {valores}")
print(f"O valor 5 FOI encontrado na lista na posição {valores.index(5)}"
      if 5 in valores else "O Valor 5 NÃO foi encontrado na lista!")