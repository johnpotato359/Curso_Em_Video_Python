count = soma = 0
while True:
    n = int(input("Digite um número (999 para parar): "))
    if n == 999:
        break
    soma += n
    count += 1
print(f"Foram {count} números digitados",
      f"\nA soma dos números é {soma}")
print("Programa finalizado")