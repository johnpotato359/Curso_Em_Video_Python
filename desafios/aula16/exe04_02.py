num = num_par = ()
num_prt = ("um", "outro", "mais um", "o último")
lista_num = list(num)
lista_num_par = list(num_par)
for i in range(0, len(num_prt)):
    n = int(input(f"Digite {num_prt[i]} número: "))
    lista_num.append(n)
    if n % 2 == 0:
        lista_num_par.append(n)
num = tuple(lista_num)
num_par = tuple(lista_num_par)
print(f"Você digitou os valores {num}")
print(f"O Valor 9 apareceu {num.count(9)} vezes")
print("O valor 3 não foi digitado em nenhuma posição"
      if 3 not in num
      else f"O valor 3 apareceu na {num.index(3)+1}ª posição")
print("Os valores pares digitados foram ", end="")
for i in range(0, len(num_par)):
    print(num_par[i], end=" ")