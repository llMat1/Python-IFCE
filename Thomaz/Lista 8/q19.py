alunos = []
qtd = int(input("Quantos alunos serão cadastrados? "))

for i in range(qtd):
    nome = input(f"\nNome do aluno {i + 1}: ")
    nota1 = float(input("Nota 1: "))
    nota2 = float(input("Nota 2: "))
    media = (nota1 + nota2) / 2
    alunos.append([nome, nota1, nota2, media])

print("\n=== Boletim da Turma ===")
for aluno in alunos:
    status = "Aprovado" if aluno[3] >= 7.0 else "Reprovado"
    print(f"Aluno: {aluno[0]} | Média: {aluno[3]:.2f} | Status: {status}")