n1 = int(input("Digite o primeiro número: "))
n2 = int(input("Digite o segundo número: "))
n3 = int(input("Digite o terceiro número: "))

soma = n1 + n2 + n3

if n1 == n2 == n3:
    soma = soma * 3

print(f"O resultado é: {soma}")