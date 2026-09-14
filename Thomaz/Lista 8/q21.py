def cadastrar(estoque: list) -> None:
    nome = input("Nome do produto: ")
    qtd = int(input("Quantidade: "))
    preco = float(input("Preço: R$ "))
    estoque.append([nome, qtd, preco])

def atualizar_qtd(estoque: list) -> None:
    nome = input("Nome do produto a atualizar: ")
    for p in estoque:
        if p[0] == nome:
            p[1] = int(input("Nova quantidade: "))
            print("Quantidade atualizada!")
            return
    print("Produto não encontrado.")

def remover(estoque: list) -> None:
    nome = input("Nome do produto a remover: ")
    for p in estoque:
        if p[0] == nome:
            estoque.remove(p)
            print("Produto removido!")
            return
    print("Produto não encontrado.")

def listar(estoque: list) -> None:
    print("\n--- Estoque ---")
    for p in estoque:
        print(f"Produto: {p[0]} | Qtd: {p[1]} | Preço: R$ {p[2]:.2f}")

estoque = []
op = ""
while op != "5":
    print("\n1. Cadastrar\n2. Atualizar Qtd\n3. Remover\n4. Listar\n5. Sair")
    op = input("Opção: ")
    if op == "1":
        cadastrar(estoque)
    elif op == "2":
        atualizar_qtd(estoque)
    elif op == "3":
        remover(estoque)
    elif op == "4":
        listar(estoque)