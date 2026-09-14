def calcular_media(lista):
    soma = 0
    for nota in lista:
        soma += nota
    return soma / len(lista)

# Leitura das notas de 10 alunos
notas = []
for i in range(10):
    nota = float(input(f"Digite a nota do aluno {i + 1}: "))
    notas.append(nota)

# Processamento com variáveis auxiliares e laços
media_turma = calcular_media(notas)

acima_media = 0
abaixo_media = 0
maior_nota = notas[0]
menor_nota = notas[0]

for nota in notas:
    if nota > media_turma:
        acima_media += 1
    elif nota < media_turma:
        abaixo_media += 1
        
    if nota > maior_nota:
        maior_nota = nota
    if nota < menor_nota:
        menor_nota = nota

# Exibição dos resultados
print("\n=== RESUMO DA TURMA ===")
print(f"Média da turma: {media_turma:.2f}")
print(f"Alunos acima da média: {acima_media}")
print(f"Alunos abaixo da média: {abaixo_media}")
print(f"Maior nota: {maior_nota:.2f}")
print(f"Menor nota: {menor_nota:.2f}")