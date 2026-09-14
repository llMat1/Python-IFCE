numeros = []
for i in range(6):
    num = int(input(f"Digite o {i + 1}º número: "))
    numeros.append(num)

print("Números pares digitados:")
for num in numeros:
    if num % 2 == 0:
        print(num)