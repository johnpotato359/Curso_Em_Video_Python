from random import randint

num_rand = ()
lista_num_rand = list(num_rand)

for i in range(0, 5):
    lista_num_rand.append(randint(0, 11))

num_rand = tuple(lista_num_rand)
print(f"Os valores sorteados foram: ", end="")
for i in range(0, len(num_rand)):
    print(num_rand[i], end=" ")
print(f"\nO MAIOR valor sorteado foi: {max(num_rand)}",
      f"\nO MENOR valor sorteado foi: {min(num_rand)}")
