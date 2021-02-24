frase = "Curso em Vídeo Python"

#Fatiamento de String

#Começa na posição 0 e imprime até a posição 13
print(frase[:14])

#Começa na posição 0 e imprime todas as posições
print(frase[0:])

#Começa na posição 15 e imprime o resto das posições
print(frase[15:])

#Começa na posição 0 e imprime até a posição 17
print(frase[0:18])

#Pulando Posições de 2 em 2| print(frase[x:y:2)
print(frase[0:14:2])

#Print com três aspas
print("""Welcome! Are you completely new to programming?
about why and how to get started with Python. Fortunately
an experienced programmer in any programming language
(whatever it may be) can pick up Python very quickly.
Its also easy for beginners to use and learn, so jump in!""")

#Contando letras específicas
print(frase.upper().count("O"))

#Retorna o tamanho da String
print(len(frase))

#Remover os espaços da String
frase = "  Curso em Vídeo Python   "
print(frase.strip())

#Replace, repor uma palavra por outra
frase = "Curso em Vídeo Python"
print(frase.replace("Python", "Android"))
#Strings são imutáveis, para mudar de fato é necessário realizar uma atribuição
frase = frase.replace("Python", "Android")

#Encontrar a posição de alguma palavra(parâmetro)
frase = "Curso em Vídeo Python"
print(frase.find("Curso"))

#Usando o Split

print(frase.split())
dividido = frase.split()
print(dividido[0])
print(dividido[0][3])

sds = 'prova de python'
print(len(sds))