numero = int(input("Digite um número (0 para sair): "))

while numero != 0:
    multiplo = numero
    print(f"Múltiplos de {numero} menores que 100:")
    while multiplo < 100:
        print(multiplo, end=" ")
        multiplo += numero
    print("\n" + "-" * 20)
    numero = int(input("Digite outro número (0 para sair): "))