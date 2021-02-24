#Exemplo01
nome = str(input("Qual é o seu nome? "))
if nome =="Nicholas":
    print("Que nome lindo você tem!")
else:
    print("Seu nome é tão normal!")
print("Bom dia, {}".format(nome))

#Exemplo02
n1 = float(input("Digite a primeira nota: "))
n2 = float(input("Digite a segunda nota: "))
m = (n1 + n2) / 2
print("A sua média foi de {:.1f}".format(m))

#Bloco IF normal
if m >= 6:
    print("A sua média está razoável")
else:
    print("A sua média está abaixo do esperado, SE EMPENHE MAIS!")

#Bloco IF Simplificado
#print("A sua média está razoável" if m >= 6
#      else "A sua média está abaixo do esperado, se EMPENHE MAIS")
