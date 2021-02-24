print("=" * 30)
print("{:^30}".format("BANCO CEV"))
print("=" * 30)
n = int(input("Qual valor deseja sacar? R$"))

while True:
    if n >= 50:
        c = n
        c = (c // 50)
        n = n - (c * 50)
        print(f"Total de {c} cédulas de R$50")
    elif n >= 20:
        v = n
        v = (v // 20)
        n = n - (v * 20)
        print(f"Total de {v} cédulas de R$20")
    elif n >= 10:
        d = n
        d = (d // 10)
        n = n - (d * 10)
        print(f"Total de {d} cédulas de R$10")
    elif n >= 1:
        u = n
        u = (u // 1)
        n = n - (u * 1)
        print(f"Total de {u} cédulas de R$1")
    else:
        break
print("="*30)
print("Volte sempre ao BANCO CEV! Tenha um bom dia!")
