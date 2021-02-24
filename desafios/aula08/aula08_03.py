import math
angulo = float(input("Digite o ângulo: "))
#Converte Radiano para Grau

print("O Valor do Seno do ângulo de {}º é = {:.2f}".format(angulo, math.sin(math.radians(angulo))),
      "\nO Valor do Cosseno do ângulo de {}º é = {:.2f}".format(angulo, math.cos(math.radians(angulo))),
      "\nO Valor da Tangente do ângulo de {}º é = {:.2f}".format(angulo, math.tan(math.radians(angulo))))