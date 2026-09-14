n = int(input("Digite um número inteiro n: "))
produto = 1

for i in range(1, n + 1):
    produto *= i

print(f"O produto acumulado de 1 até {n} é: {produto}")