numero = int(input("Digite um número inteiro: "))

if numero % 4 == 0:
    print("divisível por 4")
elif numero % 5 == 0:
    print("divisível por 5")
else:
    print("não é divisível por 4 ou 5")