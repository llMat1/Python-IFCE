estoque = []
estoque_baixo = 0

for i in range(5):
    qtd = int(input(f"Digite a quantidade em estoque do produto {i + 1}: "))
    estoque.append(qtd)
    if qtd < 10:
        estoque_baixo += 1

print(f"Quantidade de produtos com estoque menor que 10: {estoque_baixo}")