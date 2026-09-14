def validar_senha(senha):
    if len(senha) < 8:
        return False
    if " " in senha:
        return False
    
    tem_maiuscula = any(c.isupper() for c in senha)
    tem_minuscula = any(c.islower() for c in senha)
    tem_numero = any(c.isdigit() for c in senha)
    
    return tem_maiuscula and tem_minuscula and tem_numero

senha_usuario = input("Digite uma senha: ")
print(f"Senha válida: {validar_senha(senha_usuario)}")