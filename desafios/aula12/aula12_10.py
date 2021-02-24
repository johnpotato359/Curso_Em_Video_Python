from random import randint
itens = ["Pedra", "Papel", "Tesoura"]
computador = randint(0, 2)

print("[ 0 ] Pedra", "\n[ 1 ] Papel", "\n[ 2 ] Tesoura")

jogador = int(input("Qual é a sua jogada? "))

print("Você jogou {}".format(itens[jogador]))
print("O computador jogou {}".format(itens[computador]))

if jogador == computador:
    print("Empate")
elif jogador == 0 and computador == 1:
    print("Você Perdeu")
elif jogador == 1 and computador == 0:
    print("Você Ganhou")
elif jogador == 1 and computador == 2:
    print("Você Perdeu")
elif jogador == 2 and computador == 1:
    print("Você ganhou")
elif jogador == 2 and computador == 0:
    print("Você perdeu")
elif jogador == 0 and computador == 2:
    print("Você ganhou")


