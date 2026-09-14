n = int(input("Digite um número de 4 dígitos: "))

d4 = n % 10
d3 = (n // 10) % 10
d2 = (n // 100) % 10
d1 = n // 1000

if d1 == d4 and d2 == d3:
    print(f"O número {n} é um número espelho.")
else:
    print(f"O número {n} NÃO é um número espelho.")