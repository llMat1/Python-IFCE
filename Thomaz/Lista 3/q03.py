soma = 0
quantidade = 0

numero = int(input("Digite um número inteiro (-1 para encerrar): "))

while numero != -1:
    soma += numero
    quantidade += 1
    numero = int(input("Digite outro número inteiro (-1 para encerrar): "))

if quantidade > 0:
    media = soma / quantidade
    print(f"A média dos números inseridos é: {media:.2f}")
else:
    print("Nenhum número válido foi digitado.")