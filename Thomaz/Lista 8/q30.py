def obter_maior(lista: list) -> float:
    maior = lista[0]
    for x in lista[1:]:
        if x > maior:
            maior = x
    return maior

def obter_menor(lista: list) -> float:
    menor = lista[0]
    for x in lista[1:]:
        if x < menor:
            menor = x
    return menor

def obter_media(lista: list) -> float:
    soma = 0.0
    for x in lista:
        soma += x
    return soma / len(lista)

temperaturas = []
dias = ["Segunda", "Terça", "Quarta", "Quinta", "Sexta", "Sábado", "Domingo"]

for i in range(7):
    temp = float(input(f"Temperatura de {dias[i]}: "))
    temperaturas.append(temp)

maior = obter_maior(temperaturas)
menor = obter_menor(temperaturas)
media = obter_media(temperaturas)

print(f"\nMaior temperatura: {maior:.1f}°C")
print(f"Menor temperatura: {menor:.1f}°C")
print(f"Média da semana: {media:.2f}°C")

print("Dias acima da média:")
for i in range(7):
    if temperaturas[i] > media:
        print(f"- {dias[i]}: {temperaturas[i]:.1f}°C")