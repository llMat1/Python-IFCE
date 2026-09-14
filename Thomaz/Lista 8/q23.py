def buscar_produto(estoque: list, nome: str) -> int:
    for i in range(len(estoque)):
        if estoque[i][0] == nome:
            return i
    return -1