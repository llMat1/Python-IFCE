numeros = []
qtd = int(input("Quantos números deseja inserir? "))

for _ in range(qtd):
    num = int(input("Digite um número: "))
    
    posicao = 0
    while posicao < len(numeros) and numeros[posicao] < num:
        posicao += 1
        
    numeros.insert(posicao, num)

print("Lista ordenada:", numeros)