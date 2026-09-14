def contar_pares(lista):
    qtd = 0
    for num in lista:
        if num % 2 == 0:
            qtd += 1
    return qtd

numeros = []
for i in range(6):
    num = int(input(f"Digite o {i + 1}º número inteiro: "))
    numeros.append(num)

resultado = contar_pares(numeros)
print(f"A quantidade de números pares é: {resultado}")