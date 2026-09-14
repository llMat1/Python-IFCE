def validar_nome(nome):
    if len(nome) < 3:
        return False
    # Permite apenas letras e espaços
    for c in nome:
        if not (c.isalpha() or c.isspace()):
            return False
    return True

def validar_email(email):
    if "@" not in email or "." not in email or " " in email:
        return False
    return True

def validar_senha_cadastro(senha):
    if len(senha) < 8:
        return False
    
    tem_letra = any(c.isalpha() for c in senha)
    tem_numero = any(c.isdigit() for c in senha)
    
    return tem_letra and tem_numero

# --- Programa Principal ---
print("=== Cadastro de Usuário ===")
nome_in = input("Nome: ")
email_in = input("E-mail: ")
senha_in = input("Senha: ")

nome_valido = validar_nome(nome_in)
email_valido = validar_email(email_in)
senha_valida = validar_senha_cadastro(senha_in)

if nome_valido and email_valido and senha_valida:
    print("\nCadastro aceito com sucesso!")
else:
    print("\nCadastro recusado! Verifique os dados inseridos:")
    if not nome_valido:
        print("- Nome deve ter no mínimo 3 caracteres (apenas letras e espaços).")
    if not email_valido:
        print("- E-mail deve conter '@' e '.', e não pode ter espaços.")
    if not senha_valida:
        print("- Senha deve ter no mínimo 8 caracteres, contendo letras e números.")