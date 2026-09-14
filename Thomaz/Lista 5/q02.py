def mensagem_personalizada(nome):
    return f"Olá, {nome}! Como você está?"

nome_usuario = input("Digite seu nome: ")
mensagem = mensagem_personalizada(nome_usuario)
print(mensagem)