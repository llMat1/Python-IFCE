votos = []
cand_a = 0
cand_b = 0
cand_c = 0

for i in range(8):
    voto = int(input(f"Voto {i + 1} (1: Candidato A, 2: Candidato B, 3: Candidato C): "))
    votos.append(voto)
    
    if voto == 1:
        cand_a += 1
    elif voto == 2:
        cand_b += 1
    elif voto == 3:
        cand_c += 1

print(f"\nResultado da votação:")
print(f"Candidato A: {cand_a} voto(s)")
print(f"Candidato B: {cand_b} voto(s)")
print(f"Candidato C: {cand_c} voto(s)")