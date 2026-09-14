def fatorial(numero):
    if numero < 0:
        return None
    resultado = 1
    for i in range(1, numero + 1):
        resultado *= i
    return resultado

def binomio(n, p):
    if p < 0 or p > n:
        return "Erro: 'p' deve ser maior ou igual a 0 e menor ou igual a 'n'."
    
    # Aplicação da fórmula: n! / (p! * (n - p)!)
    coeficiente = fatorial(n) // (fatorial(p) * fatorial(n - p))
    return coeficiente

n_val = int(input("Digite o valor de n: "))
p_val = int(input("Digite o valor de p: "))

resultado_binomial = binomio(n_val, p_val)
print(f"O coeficiente binomial C({n_val}, {p_val}) é: {resultado_binomial}")