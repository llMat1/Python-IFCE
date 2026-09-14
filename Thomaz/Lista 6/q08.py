nome_completo = input("Digite seu nome completo: ")

# Remove espaços para contar caracteres
qtd_sem_espaço = len(nome_completo.replace(" ", ""))

print(f"Maiúsculas: {nome_completo.upper()}")
print(f"Minúsculas: {nome_completo.lower()}")
print(f"Quantidade de caracteres (sem espaços): {qtd_sem_espaço}")
print(f"Primeira letra: {nome_completo[0]}")