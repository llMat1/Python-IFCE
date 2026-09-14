numeros = []
for i in range(8):
    num = int(input(f"Digite o {i + 1}º número: "))
    numeros.append(num)

pares = []
impares = []
for num in numeros:
    if num % 2 == 0:
        pares.append(num)
    else:
        impares.append(num)

print("Lista original:", numeros)
print("Lista de pares:", pares)
print("Lista de ímpares:", impares)