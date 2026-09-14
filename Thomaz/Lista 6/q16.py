def limpar_frase(frase):
    resultado = ""
    for caractere in frase:
        if caractere.isalpha() or caractere.isspace():
            resultado += caractere
    return resultado

print(limpar_frase("Olá, turma 2026!!!"))