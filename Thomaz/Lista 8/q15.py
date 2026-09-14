nomes = ["Ana", "Carlos", "Fernanda", "Marcos"]
print("Lista atual:", nomes)

novo_nome = input("Digite o novo nome: ")
posicao = int(input(f"Digite a posição de inserção (0 a {len(nomes)}): "))

if 0 <= posicao <= len(nomes):
    nomes.insert(posicao, novo_nome)
    print("Lista atualizada:", nomes)
else:
    print("Posição inválida!")