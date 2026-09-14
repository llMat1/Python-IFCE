numeros = []
qtd_pares = 0

for i in range(8):
    num = int(input(f"Digite o {i + 1}º número inteiro: "))
    numeros.append(num)
    if num % 2 == 0:
        qtd_pares += 1

print(f"Existem {qtd_pares} números pares na lista.")