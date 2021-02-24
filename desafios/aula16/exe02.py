times = ("Internacional", "Flamengo", "Atlético Mineiro", "São Paulo",
         "Fluminense", "Palmeiras", "Grêmio", "Athletico Paranaense",
         "Ceará", "Corinthians", "Santos", "Atlético Goianiense",
         "Bragantino", "Vasco", "Bahia", "Sport", "Fortaleza",
         "Goiás", "Coritiba", "Botafogo")

print(f"Os CINCO primeiros colocados: {times[:5]}")
print(f"Os QUATRO últimos colocados: {times[16:]}")
print(f"Times em ordem ALFABÉTICA: {sorted(times)}")
print(f"O Coritiba está na {times.index('Coritiba')}ª posição")

