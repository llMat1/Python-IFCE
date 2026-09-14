n = int(input("Digite um número inteiro N: "))

soma_divisores = 0
divisor = 1

while divisor < n:
    if n % divisor == 0:
        soma_divisores += divisor
    divisor += 1

if soma_divisores == n and n > 0:
    print(f"{n} é um número perfeito.")
else:
    print(f"{n} NÃO é um número perfeito.")