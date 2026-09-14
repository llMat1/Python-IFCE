numeros = []

for i in range(6):
    num = int(input(f"Digite o {i + 1}º número inteiro: "))
    numeros.append(num)

busca = int(input("Digite o número que deseja buscar: "))

if busca in numeros:
    print(f"O número {busca} aparece na lista!")
else:
    print(f"O número {busca} NÃO aparece na lista.")