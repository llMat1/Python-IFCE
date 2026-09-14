def adicionar_filme(banco: list) -> None:
    titulo = input("Título: ")
    diretor = input("Diretor: ")
    ano = input("Ano: ")
    genero = input("Gênero: ")

    if titulo != "" and diretor != "" and ano != "" and genero != "":
        banco.append([titulo, diretor, ano, genero])
        print("Filme cadastrado com sucesso!")
    else:
        print("Erro: Nenhum campo pode ficar vazio!")

def pesquisar_genero(banco: list) -> None:
    genero = input("Digite o gênero para busca: ")
    encontrados = False
    for f in banco:
        if f[3].lower() == genero.lower():
            print(f"- {f[0]} ({f[2]}) | Diretor: {f[1]}")
            encontrados = True
    if not encontrados:
        print("Nenhum filme encontrado para esse gênero.")

def listar_filmes(banco: list) -> None:
    print("\n--- Todos os Filmes ---")
    for f in banco:
        print(f"Título: {f[0]} | Diretor: {f[1]} | Ano: {f[2]} | Gênero: {f[3]}")

filmes = []
op = ""
while op != "4":
    print("\n1. Adicionar Filme\n2. Pesquisar por Gênero\n3. Listar Todos\n4. Sair")
    op = input("Opção: ")
    if op == "1":
        adicionar_filme(filmes)
    elif op == "2":
        pesquisar_genero(filmes)
    elif op == "3":
        listar_filmes(filmes)