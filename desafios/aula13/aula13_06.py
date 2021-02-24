primeiro = int(input("Insira o primeiro termo: "))
razao = int(input("Insira a razão: "))
decimo = primeiro + (10 - 1) * razao

for c in range (primeiro, 10 + razao, razao):
    print(c)