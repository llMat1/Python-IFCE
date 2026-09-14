def adicionar_item(compras: list) -> None:
    item = input("Digite o item para adicionar: ")
    compras.append(item)
    print("Item adicionado!")

def remover_item(compras: list) -> None:
    item = input("Digite o item para remover: ")
    if item in compras:
        compras.remove(item)
        print("Item removido!")
    else:
        print("Item não encontrado.")

def exibir_lista(compras: list) -> None:
    print("\n--- Lista de Compras ---")
    for item in compras:
        print(f"- {item}")

lista_compras = []
opcao = ""
while opcao != "4":
    print("\n1. Adicionar item\n2. Remover item\n3. Exibir lista\n4. Encerrar")
    opcao = input("Opção: ")
    if opcao == "1":
        adicionar_item(lista_compras)
    elif opcao == "2":
        remover_item(lista_compras)
    elif opcao == "3":
        exibir_lista(lista_compras)