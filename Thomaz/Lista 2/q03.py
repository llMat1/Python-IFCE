numero = int(input("Digite um número inteiro: "))

if 50 <= numero <= 100:
    print("entre 50 e 100")
elif numero < 0 or numero > 200:
    print("menor que 0 ou maior que 200")
else:
    print("fora das condições anteriores")