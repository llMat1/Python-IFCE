inicio = int(input("Digite o início do intervalo: "))
fim = int(input("Digite o fim do intervalo: "))

print(f"Números narcisistas no intervalo de {inicio} a {fim}:")

for num in range(inicio, fim + 1):
    str_num = str(num)
    qtd_digitos = len(str_num)
    soma_potencias = 0
    
    for digito in str_num:
        soma_potencias += int(digito) ** qtd_digitos
        
    if soma_potencias == num:
        print(num)