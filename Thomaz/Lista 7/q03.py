numeros = []

for i in range(5):
    num = int(input(f"Digite o {i + 1}º número inteiro: "))
    numeros.append(num)

maior = max(numeros)
print(f"O maior número da lista é: {maior}")