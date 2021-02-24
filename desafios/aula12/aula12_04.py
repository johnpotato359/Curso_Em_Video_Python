from datetime import datetime
anoNasc = int(input("Digite o ano de Nascimento: "))
anoAtual = datetime.today().year
idade = anoAtual-anoNasc
tempoFalta = 18 - idade
tempoPassou = idade - 18
if idade < 18:
    print("Ainda não é hora de se alistar")
    print("Faltam {} anos para se alistar".format(tempoFalta))
elif idade == 18:
    print("Agora é a hora de se Alistar")
else:
    print("Você passou {} anos do tempo de se alistar".format(tempoPassou))