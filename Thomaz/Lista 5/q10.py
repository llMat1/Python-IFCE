def fibonacci(n):
    if n <= 0:
        return []
    elif n == 1:
        return [0]
    
    sequencia = [0, 1]
    for i in range(2, n):
        proximo = sequencia[-1] + sequencia[-2]
        sequencia.append(proximo)
        
    return sequencia

n_termos = int(input("Digite a quantidade de termos da sequência de Fibonacci: "))
resultado = fibonacci(n_termos)
print(f"Sequência de Fibonacci com {n_termos} termo(s): {resultado}")