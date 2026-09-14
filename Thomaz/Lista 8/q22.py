matriz = []
for i in range(3):
    linha = []
    for j in range(3):
        val = int(input(f"Digite o elemento [{i}][{j}]: "))
        linha.append(val)
    matriz.append(linha)

print("\n--- Matriz 3x3 ---")
for linha in matriz:
    print(linha)

soma_total = 0
diagonal = []
for i in range(3):
    for j in range(3):
        soma_total += matriz[i][j]
        if i == j:
            diagonal.append(matriz[i][j])

print(f"Soma de todos os elementos: {soma_total}")
print("Elementos da diagonal principal:", diagonal)