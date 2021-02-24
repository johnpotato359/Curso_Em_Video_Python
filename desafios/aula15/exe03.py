from random import randint
from time import sleep
vit = 0
while True:
    print("=-=" * 10)
    n = int(input("Diga um valor: "))
    paim = str(input("Par ou Ímpar? [P/I]: ")).upper()
    r = randint(0, 10)
    nr = n + r

    if nr % 2 == 0 and "P" in paim:
        print("Você venceu!",
              f"\nVocê jogou {n} e a máquina {r}. Total de {nr}, DEU PAR",
              "\nVamos jogar novamente...")
        vit += 1
        sleep(3)
    elif nr % 2 == 1 and "I" in paim:
        print("Você venceu!",
              f"\nVocê jogou {n} e a máquina {r}. Total de {nr}, DEU ÍMPAR",
              "\nVamos jogar novamente...")
        sleep(3)
        vit += 1
    else:
        print(f"Você jogou {n} e a máquina {r}. Total de {nr}, DEU ÍMPAR",
              "\nVocê PERDEU!", f"Você venceu {vit} vezes.")
        break
