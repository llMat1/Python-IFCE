from random import randint

def jogo_adivinhacao():
    numero_secreto = randint(1, 100)
    tentativas = 0
    acertou = False
    
    print("Jogo de Adivinhação! Tente adivinhar o número entre 1 e 100.")
    
    while not acertou:
        palpite = int(input("Digite seu palpite: "))
        tentativas += 1
        
        if palpite < numero_secreto:
            print("Muito baixo! Tente um número maior.")
        elif palpite > numero_secreto:
            print("Muito alto! Tente um número menor.")
        else:
            acertou = True
            print(f"Parabéns! Você acertou o número {numero_secreto} em {tentativas} tentativa(s).")

# Executa o jogo
jogo_adivinhacao()