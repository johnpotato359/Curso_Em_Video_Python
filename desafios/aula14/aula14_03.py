from time import sleep
n1 = float(input("Digite N1: "))
n2 = float(input("Digite N2: "))
r = 0

while r == 0:
    sleep(3)
    print("=" * 10, "Menu", "=" * 10)
    print("[1] Somar",
          "\n[2] Multiplicar",
          "\n[3] Maior",
          "\n[4] Novos números",
          "\n[5] Sair do programa")
    r = int(input("Selecione uma opção: "))

    if r == 1:
        print("A soma de {} e {} é = {}".format(n1, n2, n1+n2))
        r = 0

    elif r == 2:
        print("A Multiplicação de {} e {} é = {}".format(n1, n2, n1*n2))
        r = 0

    elif r == 3:
        if n1 > n2:
            print("Entre {} e {} o maior é {}".format(n1, n2, n1))
        else:
            print("Entre {} e {} o maior é {}".format(n1, n2, n2))
        r = 0

    elif r == 4:
        n1 = float(input("Digite novos números para N1: "))
        n2 = float(input("Digite novos números para N2: "))
        r = 0

    elif r == 5:
        print("Saindo do programa...")
        sleep(2)
    else:
        print("Opção Inválida. Tente novamente!")
        r = 0