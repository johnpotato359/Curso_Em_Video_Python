nome = str(input("Digite o seu Nome Completo: "))
lista = nome.split()
print("Seu Primeiro nome é {}".format(lista[0]),
      "\nSeu Último nome é {}".format(lista[len(lista)-1]))