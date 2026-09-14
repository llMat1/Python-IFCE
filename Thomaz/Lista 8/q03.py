frutas = ["maçã", "banana", "laranja", "uva", "manga"]
fruta_busca = input("Digite o nome de uma fruta: ")

if fruta_busca in frutas:
    frutas.remove(fruta_busca)
    print("Fruta removida! Lista atualizada:", frutas)
else:
    print("A fruta não foi encontrada na lista.")