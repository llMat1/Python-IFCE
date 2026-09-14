def cadastrar_contato(agenda: list) -> None:
    nome = input("Nome: ")
    if nome == "":
        print("Erro: O nome não pode ser vazio!")
        return
    telefone = input("Telefone: ")
    email = input("E-mail: ")
    agenda.append([nome, telefone, email])
    print("Contato cadastrado!")

def pesquisar_contato(agenda: list) -> None:
    nome = input("Digite o nome para pesquisar: ")
    for c in agenda:
        if c[0].lower() == nome.lower():
            print(f"Encontrado: Nome: {c[0]} | Tel: {c[1]} | Email: {c[2]}")
            return
    print("Contato não encontrado.")

def editar_contato(agenda: list) -> None:
    nome = input("Digite o nome do contato que deseja editar: ")
    for c in agenda:
        if c[0].lower() == nome.lower():
            c[1] = input("Novo Telefone: ")
            c[2] = input("Novo E-mail: ")
            print("Contato atualizado!")
            return
    print("Contato não encontrado.")

def remover_contato(agenda: list) -> None:
    nome = input("Digite o nome do contato a remover: ")
    for c in agenda:
        if c[0].lower() == nome.lower():
            agenda.remove(c)
            print("Contato removido!")
            return
    print("Contato não encontrado.")

agenda = []
op = ""
while op != "5":
    print("\n1. Cadastrar\n2. Pesquisar\n3. Editar\n4. Remover\n5. Sair")
    op = input("Opção: ")
    if op == "1":
        cadastrar_contato(agenda)
    elif op == "2":
        pesquisar_contato(agenda)
    elif op == "3":
        editar_contato(agenda)
    elif op == "4":
        remover_contato(agenda)