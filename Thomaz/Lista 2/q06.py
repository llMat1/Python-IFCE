n = int(input("Digite um número de 4 dígitos: "))

d4 = n % 10
d3 = (n // 10) % 10
d2 = (n // 100) % 10
d1 = n // 1000

if d1 != d2 and d1 != d3 and d1 != d4 and d2 != d3 and d2 != d4 and d3 != d4:
    print("Todos os dígitos são diferentes.")
else:
    print("Existem dígitos repetidos.")