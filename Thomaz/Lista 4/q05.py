n = int(input("Digite um número inteiro: "))
soma_divisores = 0

for i in range(1, n):
    if n % i == 0:
        soma_divisores += i

if soma_divisores == n and n > 0:
    print(f"{n} é um número perfeito.")
else:
    print(f"{n} NÃO é um número perfeito.")