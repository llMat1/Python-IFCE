inicio = int(input("Digite o início do intervalo: "))
fim = int(input("Digite o fim do intervalo: "))

print(f"Números perfeitos entre {inicio} e {fim}:")

atual = inicio
while atual <= fim:
    soma_divisores = 0
    divisor = 1
    
    while divisor < atual:
        if atual % divisor == 0:
            soma_divisores += divisor
        divisor += 1
        
    if soma_divisores == atual and atual > 0:
        print(atual)
        
    atual += 1