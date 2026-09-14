n = int(input("Digite um número inteiro: "))
soma = 0

for i in range(0, n + 1, 3):
    soma += i

print(f"A soma dos múltiplos de 3 até {n} é: {soma}")