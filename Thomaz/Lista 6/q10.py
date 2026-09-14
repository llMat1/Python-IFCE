def contar_caracteres(texto):
    contador = 0
    for _ in texto:
        contador += 1
    return contador

palavra = input("Digite uma palavra: ")
tamanho = contar_caracteres(palavra)
print(f"A palavra possui {tamanho} caracteres.")