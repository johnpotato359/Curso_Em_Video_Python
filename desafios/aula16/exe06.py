palavras = ("programador", "guanabara", "malako", "bijuteria",
            "biluteteia", "xogros", "pilantra", "sabotage",
            "senpai", "biruleibe", "ouldri", "kandra", "larray")
for j in range(0, len(palavras)):
    print(f"\nNa palavra {palavras[j].upper()} temos: ", end="")
    for i in range(0, len(palavras[j])):
        if palavras[j][i] in "aeiou":
             print(palavras[j][i], end=" ")
