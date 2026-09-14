def conversor_moeda(valor_brl, taxa_cambio):
    return valor_brl / taxa_cambio

brl = float(input("Digite o valor em Reais (BRL): R$ "))
taxa = float(input("Digite a taxa de câmbio (preço de 1 USD em BRL): R$ "))

usd = conversor_moeda(brl, taxa)
print(f"O valor equivalente em dólares é: US$ {usd:.2f}")