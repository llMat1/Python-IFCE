produtos = []
precos = []

while True:
    prod = input("Digite o nome do produto (ou 'sair' para encerrar): ")
    if prod.lower() == "sair":
        break
    preco = float(input(f"Digite o preço de {prod}: R$ "))
    produtos.append(prod)
    precos.append(preco)

print("\nProdutos com preço maior que R$ 50,00:")
for i in range(len(produtos)):
    if precos[i] > 50.0:
        print(f"- {produtos[i]}: R$ {precos[i]:.2f}")