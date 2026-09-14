n = int(input("Digite um número de 5 dígitos (ex: 73845): "))

d5 = n % 10
n = n // 10

d4 = n % 10
n = n // 10

d3 = n % 10
n = n // 10

d2 = n % 10
d1 = n // 10

soma = d1 + d2 + d3 + d4 + d5
print(f"A soma dos dígitos é: {soma}")