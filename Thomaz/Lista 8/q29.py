def adicionar_item(carrinho: list) -> None:
    nome = input("Nome do item: ")
    qtd = int(input("Quantidade: "))
    preco = float(input("Preço unitário: R$ "))
    carrinho.append([nome, qtd, preco])

def remover_item(carrinho: list) -> None:
    nome = input("Nome do item a remover: ")
    for item in carrinho:
        if item[0].lower() == nome.lower():
            carrinho.remove(item)
            print("Item removido!")
            return
    print("Item não encontrado.")

def alterar_qtd(carrinho: list) -> None:
    nome = input("Nome do item: ")
    for item in carrinho:
        if item[0].lower() == nome.lower():
            item[1] = int(input("Nova quantidade: "))
            print("Quantidade alterada!")
            return
    print("Item não encontrado.")

def calcular_total(carrinho: list) -> None:
    total = 0.0
    print("\n--- Itens no Carrinho ---")
    for item in carrinho:
        subtotal = item[1] * item[2]
        total += subtotal
        print(f"Item: {item[0]} | Qtd: {item[1]} | R$ {item[2]:.2f} un. | Subtotal: R$ {subtotal:.2f}")
    print(f"VALOR TOTAL DA COMPRA: R$ {total:.2f}")

carrinho = []
op = ""
while op != "5":
    print("\n1. Adicionar Item\n2. Remover Item\n3. Alterar Quantidade\n4. Calcular Total\n5. Sair")
    op = input("Opção: ")
    if op == "1":
        adicionar_item(carrinho)
    elif op == "2":
        remover_item(carrinho)
    elif op == "3":
        alterar_qtd(carrinho)
    elif op == "4":
        calcular_total(carrinho)