def fatorial(numero):
    if numero < 0:
        return "Não existe fatorial de número negativo."
    resultado = 1
    for i in range(1, numero + 1):
        resultado *= i
    return resultado

num = int(input("Digite um número inteiro não negativo: "))
res = fatorial(num)
print(f"O fatorial de {num} é: {res}")