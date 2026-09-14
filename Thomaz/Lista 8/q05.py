def mostrar_lista(itens: list) -> None:
    for i in range(len(itens)):
        print(f"{i} -> {itens[i]}")

# Teste da função
mostrar_lista(["João", "Maria", "Pedro"])