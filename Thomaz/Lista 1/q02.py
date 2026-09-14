preco_capa = 32.90
desconto = 0.35
copias = 75

preco_com_desconto = preco_capa * (1 - desconto)

# Transporte: R$ 4,00 para o 1º exemplar + R$ 0,80 para os 74 restantes
custo_transporte = 4.00 + (copias - 1) * 0.80

custo_total = (preco_com_desconto * copias) + custo_transporte
print(f"O custo total de atacado para {copias} cópias é: R$ {custo_total:.2f}")