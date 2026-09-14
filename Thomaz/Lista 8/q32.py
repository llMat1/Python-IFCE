matriz = []
for i in range(4):
    linha = []
    for j in range(4):
        val = int(input(f"Digite o valor [{i}][{j}]: "))
        linha.append(val)
    matriz.append(linha)

print("\n--- Matriz Completa ---")
for linha in matriz:
    print(linha)

print("\n--- Soma das Linhas ---")
for i in range(4):
    soma_linha = 0
    for j in range(4):
        soma_linha += matriz[i][j]
    print(f"Soma da Linha {i}: {soma_linha}")

print("\n--- Soma das Colunas ---")
for j in range(4):
    soma_coluna = 0
    for i in range(4):
        soma_coluna += matriz[i][j]
    print(f"Soma da Coluna {j}: {soma_coluna}")

maior_valor = matriz[0][0]
linha_maior = 0
coluna_maior = 0

for i in range(4):
    for j in range(4):
        if matriz[i][j] > maior_valor:
            maior_valor = matriz[i][j]
            linha_maior = i
            coluna_maior = j

print(f"\nMaior valor: {maior_valor}")
print(f"Encontrado na Linha {linha_maior}, Coluna {coluna_maior}")