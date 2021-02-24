n1 = 10
n2 = 5

soma = n1 + n2
subtracao = n1 - n2
multiplicacao = n1 * n2
divisao = n1 / n2
exponenciacao = n1 ** n2
divInteira = n1 // n2
modulo = n1 % n2



print(soma)
print(subtracao)
print(multiplicacao)
print(divisao)
print(exponenciacao)
print(divInteira)
print(modulo)

print("A soma é {}, subtracao {}, multiplicacao {}, divisao {}, exponenciacao {}, divInteira {} e modulo {}"
      .format(soma, subtracao, multiplicacao, divisao, exponenciacao, divInteira, modulo))
#Delimitar as casas decimais {:.3f}
#Replicando informacoes

nome = input("Digite o seu nome: ")
print("Prazer em te conhecer {:^20}!".format(nome))
print("Prazer em te conhecer {:>20}!".format(nome))
print("Prazer em te conhecer {:<20}!".format(nome))