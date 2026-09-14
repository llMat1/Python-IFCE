def eh_palindromo(palavra):
    palavra_limpa = palavra.lower().replace(" ", "")
    return palavra_limpa == palavra_limpa[::-1]

print(eh_palindromo("arara"))  # True
print(eh_palindromo("python")) # False