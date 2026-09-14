n = int(input("Digite um número inteiro n: "))
somatoria = 0

for i in range(1, n):
    if i % 4 == 0 or i % 6 == 0:
        somatoria += i

print(f"A soma dos números menores que {n} divisíveis por 4 ou 6 é: {somatoria}")