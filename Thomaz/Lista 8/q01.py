alunos = []
for i in range(5):
    nome = input(f"Digite o nome do aluno {i + 1}: ")
    alunos.append(nome)

print("Lista completa:", alunos)
print("Primeiro nome cadastrado:", alunos[0])
print("Último nome cadastrado:", alunos[-1])