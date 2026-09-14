numeros = []
while True:
    num = int(input("Digite um número inteiro (0 para parar): "))
    if num == 0:
        break
    numeros.append(num)

print("Lista de números digitados:", numeros)