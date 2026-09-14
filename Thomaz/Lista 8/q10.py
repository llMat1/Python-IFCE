nomes = []
while True:
    nome = input("Digite um nome (ou 'fim' para encerrar): ")
    if nome.lower() == "fim":
        break
    nomes.append(nome)

pesquisa = input("Digite um nome para pesquisar: ")
if pesquisa in nomes:
    print(f"O nome {pesquisa} ESTÁ na lista.")
else:
    print(f"O nome {pesquisa} NÃO está na lista.")