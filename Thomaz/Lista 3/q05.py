n = int(input("Digite um número para calcular o fatorial: "))

fatorial = 1
contador = n

while contador > 1:
    fatorial *= contador
    contador -= 1

print(f"O fatorial de {n} é: {fatorial}")