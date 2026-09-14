notas = []
aprovados = 0

for i in range(6):
    nota = float(input(f"Digite a nota do aluno {i + 1}: "))
    notas.append(nota)
    if nota >= 7:
        aprovados += 1

print(f"Quantidade de alunos aprovados (nota >= 7): {aprovados}")