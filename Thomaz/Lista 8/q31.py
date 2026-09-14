def cadastrar_livro(bib: list) -> None:
    titulo = input("Título: ")
    autor = input("Autor: ")
    ano = input("Ano: ")
    bib.append([titulo, autor, ano, "disponível"])
    print("Livro cadastrado!")

def emprestar_livro(bib: list) -> None:
    titulo = input("Título do livro: ")
    for livro in bib:
        if livro[0].lower() == titulo.lower():
            if livro[3] == "disponível":
                livro[3] = "emprestado"
                print("Livro emprestado com sucesso!")
            else:
                print("Livro já se encontra emprestado!")
            return
    print("Livro não encontrado.")

def devolver_livro(bib: list) -> None:
    titulo = input("Título do livro: ")
    for livro in bib:
        if livro[0].lower() == titulo.lower():
            if livro[3] == "emprestado":
                livro[3] = "disponível"
                print("Livro devolvido com sucesso!")
            else:
                print("Este livro já está disponível.")
            return
    print("Livro não encontrado.")

def pesquisar_livro(bib: list) -> None:
    titulo = input("Título do livro: ")
    for livro in bib:
        if livro[0].lower() == titulo.lower():
            print(f"Título: {livro[0]} | Autor: {livro[1]} | Ano: {livro[2]} | Situação: {livro[3]}")
            return
    print("Livro não encontrado.")

def listar_livros(bib: list) -> None:
    print("\n--- Acervo da Biblioteca ---")
    for livro in bib:
        print(f"Título: {livro[0]} | Autor: {livro[1]} | Ano: {livro[2]} | Status: {livro[3]}")

biblioteca = []
op = ""
while op != "6":
    print("\n1. Cadastrar\n2. Emprestar\n3. Devolver\n4. Pesquisar\n5. Listar\n6. Sair")
    op = input("Opção: ")
    if op == "1":
        cadastrar_livro(biblioteca)
    elif op == "2":
        emprestar_livro(biblioteca)
    elif op == "3":
        devolver_livro(biblioteca)
    elif op == "4":
        pesquisar_livro(biblioteca)
    elif op == "5":
        listar_livros(biblioteca)