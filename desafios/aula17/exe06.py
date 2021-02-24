valores = []
valores.append(str(input("Insira sua expressão: ")))
if valores[0].count("(") % 2 == 0 and valores[0].count(")") % 2 == 0:
    print("Expressão correta")
else:
    print("Expressão incorreta")
