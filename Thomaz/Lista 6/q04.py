palavra = input("Digite uma palavra: ")

if palavra:
    nova_palavra = palavra[:-1] + "#"
    print(nova_palavra)