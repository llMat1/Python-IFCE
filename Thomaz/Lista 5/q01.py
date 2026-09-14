def calculadora(num1, num2, operacao):
    if operacao == "soma":
        return num1 + num2
    elif operacao == "subtracao":
        return num1 - num2
    elif operacao == "multiplicacao":
        return num1 * num2
    elif operacao == "divisao":
        if num2 != 0:
            return num1 / num2
        else:
            return "Erro: divisão por zero!"
    else:
        return "Operação inválida!"

n1 = float(input("Digite o primeiro número: "))
n2 = float(input("Digite o segundo número: "))
op = input("Digite a operação (soma, subtracao, multiplicacao, divisao): ").lower().strip()

resultado = calculadora(n1, n2, op)
print(f"Resultado: {resultado}")