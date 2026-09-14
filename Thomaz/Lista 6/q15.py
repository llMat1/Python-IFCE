def validar_codigo(codigo):
    if len(codigo) == 6 and codigo[:2].isalpha() and codigo[2:].isdigit():
        return "Válido"
    return "Inválido"

print(validar_codigo("AB1234"))  # Válido
print(validar_codigo("A12345"))  # Inválido