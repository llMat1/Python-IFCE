def adicionar_pessoa(fila: list) -> None:
    nome = input("Digite o nome da pessoa: ")
    fila.append(nome)
    print("Pessoa adicionada ao final da fila.")

def atender_pessoa(fila: list) -> None:
    if len(fila) > 0:
        atendido = fila.pop(0)
        print(f"Atendendo: {atendido}")
    else:
        print("Fila vazia!")

def mostrar_fila(fila: list) -> None:
    print("\nFila atual:", fila)

fila_atendimento = []
opcao = ""
while opcao != "4":
    print("\n1. Adicionar pessoa\n2. Atender pessoa\n3. Mostrar fila\n4. Sair")
    opcao = input("Opção: ")
    if opcao == "1":
        adicionar_pessoa(fila_atendimento)
    elif opcao == "2":
        atender_pessoa(fila_atendimento)
    elif opcao == "3":
        mostrar_fila(fila_atendimento)