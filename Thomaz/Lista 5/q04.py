def eh_par(numero):
    if numero % 2 == 0:
        print("Verdade, é par")
    else:
        print("Falso, é ímpar")

num = int(input("Digite um número inteiro: "))
eh_par(num)