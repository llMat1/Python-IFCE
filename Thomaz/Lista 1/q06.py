base_maior = float(input("Digite o valor da base maior (B): "))
base_menor = float(input("Digite o valor da base menor (b): "))
altura = float(input("Digite o valor da altura (h): "))

area = ((base_maior + base_menor) * altura) / 2
print(f"A área do trapézio é: {area:.2f}")