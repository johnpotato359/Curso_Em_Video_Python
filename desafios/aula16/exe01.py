num = ("zero", "um", "dois", "três", "quatro", "cinco", "seis", "sete", "oito",
       "nove", "dez", "onze", "doze", "treze", "quatorze", "quinze", "dezesseis",
       "dezesete", "dezoito", "dezenove", "vinte")
while True:
    n = int(input("Digite um número entre 0 e 20: "))
    while n < 0 or n > 20:
        n = int(input("Tente novamente. Digite um número entre 0 e 20: "))
    print(f"Você digitou o número {num[n]}")
    resp = " "
    resp = str(input("Quer outro número?[S/N] ")).strip().upper()[0]
    if resp in "N":
        print("PROGRAMA FINALIZADO")
        break
