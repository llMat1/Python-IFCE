def gerar_usuario(nome, sobrenome):
    usuario = nome[:3] + sobrenome[-3:]
    return usuario.lower()

nome_input = input("Nome: ")
sobrenome_input = input("Sobrenome: ")

print(f"Resultado: {gerar_usuario(nome_input, sobrenome_input)}")