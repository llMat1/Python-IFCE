numeros = []
for i in range(10):
    num = int(input(f"Digite o {i + 1}º número: "))
    numeros.append(num)

i = 0
while i < len(numeros):
    if numeros[i] < 0:
        numeros.pop(i)
    else:
        i += 1

print("Lista sem números negativos:", numeros)