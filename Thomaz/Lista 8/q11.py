def contar_ocorrencias(lista: list, valor: str) -> int:
    contador = 0
    for item in lista:
        if item == valor:
            contador += 1
    return contador

# Exemplo de teste:
# print(contar_ocorrencias(["a", "b", "a"], "a"))