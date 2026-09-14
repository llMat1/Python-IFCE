import random

num_secreto = random.randint(10, 50)
palpite = int(input("Adivinhe o número secreto (entre 10 e 50): "))

while palpite != num_secreto:
    if palpite < num_secreto:
        print("O palpite é MENOR que o número secreto.")
    else:
        print("O palpite é MAIOR que o número secreto.")
    
    palpite = int(input("Tente novamente: "))

print("Parabéns! Você acertou o número secreto!")