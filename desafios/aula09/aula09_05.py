frase = str(input("Digite uma frase: ")).upper().strip()
print("Quantidade de Letra A: {}".format(frase.count("A"))
      , "\nPosição que aparece na primeira vez: {}".format(frase.find("A")+1)
      , "\nPosição que aparece na última vez: {}".format(frase.rfind("A")+1))

