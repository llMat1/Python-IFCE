def determinar_situacao(media: float) -> str:
    if media >= 7.0:
        return "Aprovado"
    elif 5.0 <= media < 7.0:
        return "Recuperação"
    else:
        return "Reprovado"

def cadastrar_boletim() -> list:
    boletim = []
    qtd = int(input("Quantos alunos serão cadastrados? "))
    for i in range(qtd):
        nome = input(f"\nNome do aluno {i + 1}: ")
        notas = []
        soma = 0.0
        for j in range(3):
            n = float(input(f"Nota {j + 1}: "))
            notas.append(n)
            soma += n
        media = soma / 3.0
        situacao = determinar_situacao(media)
        boletim.append([nome, notas, media, situacao])
    return boletim

def exibir_boletim(boletim: list) -> None:
    print("\n=== BOLETIM ESCOLAR ===")
    for aluno in boletim:
        print(f"Aluno: {aluno[0]} | Notas: {aluno[1]} | Média: {aluno[2]:.2f} | Situação: {aluno[3]}")

boletim = cadastrar_boletim()
exibir_boletim(boletim)