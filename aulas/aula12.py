nome = str(input("Qual é o seu nome? "))
if nome == "Nicholas":
    print("Que nome bonito!")
elif nome == "Pedro" or nome == "Paulo" or nome == "Maria":
    print("Seu nome é bem popular no Brasil.")
elif nome in "Ana Cláudia Jéssica Juliana":
    print("Belo nome feminino")
else:
    print("Seu nome é bem normal.")
print("Tenha um bom dia, {}".format(nome))
