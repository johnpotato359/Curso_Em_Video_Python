l = float(input("Digite a largura da parede em metros: "))
h = float(input("Digite a altura da parede em metros: "))
a = l * h

print("A Largura da Parede é {:.1f}m".format(l), "\nA Altura da Parede é {:.1f}m".format(h)
      ,"\nA Área é: {:.1f}m²".format(a)
      ,"\nSerá necessário {:.3f} litros de tinta".format(a/2))