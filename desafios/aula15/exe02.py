print("-" * 10, "TABUADA", "-" * 10)
n = int(input("Digite um número para mostrar a tabuada: "))
count = 1
while True:
    if n < 0:
        print("Tabuada encerrada!")
        break
    print(f"{n} X {count} = {n * count}")
    count += 1
    if count > 10:
        n = int(input("Quer ver a tabuada de qual valor: "))
        count = 1
