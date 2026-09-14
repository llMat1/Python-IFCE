def contar_digitos(numero):
    # Tratamento para números negativos e zero
    numero = abs(numero)
    if numero == 0:
        return 1
    
    qtd = 0
    while numero > 0:
        qtd += 1
        numero //= 10
    return qtd

num = int(input("Digite um número inteiro: "))
qtd_digitos = contar_digitos(num)
print(f"O número digitado possui {qtd_digitos} dígito(s).")