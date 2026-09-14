notas = []

for i in range(4):
    nota = float(input(f"Digite a nota {i + 1}: "))
    notas.append(nota)

media = sum(notas) / len(notas)

print(f"Média: {media:.2f}")
if media >= 6:
    print("Situação: Aprovado")
else:
    print("Situação: Reprovado")