def maior_valor(numeros: list) -> int:
    maior = numeros[0]
    for num in numeros[1:]:
        if num > maior:
            maior = num
    return maior