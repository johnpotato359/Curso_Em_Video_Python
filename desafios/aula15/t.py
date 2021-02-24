from random import randint
r = randint(0, 10)
count = 0
while True:
    r = randint(0, 10)
    print(r)
    count += 1
    if r == 10:
        break
print(f"Foram {count} tentativas")
