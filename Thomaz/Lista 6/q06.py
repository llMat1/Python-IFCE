frase = input("Digite uma frase: ")
vogais = "aeiouAEIOU"
total_vogais = 0

for caractere in frase:
    if caractere in vogais:
        total_vogais += 1

print(f"Total de vogais: {total_vogais}")