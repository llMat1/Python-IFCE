numeros = []

for i in range(5):
    num = int(input(f"Digite o {i + 1}º número inteiro: "))
    numeros.append(num)

maior = numeros[0]
indice_maior = 0

for i in range(1, len(numeros)):
    if numeros[i] > maior:
        maior = numeros[i]
        indice_maior = i

print(f"Maior número: {maior}")
print(f"Índice onde ele está: {indice_maior}")