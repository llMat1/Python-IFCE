numero = int(input("Digite um número decimal positivo: "))

if numero == 0:
    binario = "0"
else:
    binario = ""
    temp = numero
    while temp > 0:
        resto = temp % 2
        binario = str(resto) + binario
        temp = temp // 2

print(f"O número {numero} em binário é: {binario}")