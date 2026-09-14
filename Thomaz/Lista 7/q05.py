temperaturas = []

for i in range(7):
    temp = float(input(f"Digite a temperatura do dia {i + 1}: "))
    temperaturas.append(temp)

media_semana = sum(temperaturas) / len(temperaturas)
dias_acima = 0

for temp in temperaturas:
    if temp > media_semana:
        dias_acima += 1

print(f"Média da semana: {media_semana:.2f}°C")
print(f"Dias com temperatura acima da média: {dias_acima}")