texto = input("Digite algo: ")

letras = 0
numeros = 0
outros = 0

for c in texto:
    if c.isalpha():
        letras += 1
    elif c.isdigit():
        numeros += 1
    else:
        outros += 1

print(f"Letras: {letras}")
print(f"Números: {numeros}")
print(f"Outros caracteres: {outros}")