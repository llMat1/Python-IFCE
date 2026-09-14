assentos = []
for i in range(20):
    assentos.append("livre")

def mostrar_assentos(assentos: list) -> None:
    print("\n--- Estado dos Assentos ---")
    for i in range(len(assentos)):
        print(f"Assento {i + 1}: {assentos[i]}")

def reservar(assentos: list) -> None:
    num = int(input("Número do assento (1 a 20): ")) - 1
    if 0 <= num < 20:
        if assentos[num] == "livre":
            assentos[num] = "ocupado"
            print("Assento reservado com sucesso!")
        else:
            print("Erro: Assento já está ocupado!")
    else:
        print("Assento inválido!")

def cancelar(assentos: list) -> None:
    num = int(input("Número do assento (1 a 20): ")) - 1
    if 0 <= num < 20:
        if assentos[num] == "ocupado":
            assentos[num] = "livre"
            print("Reserva cancelada!")
        else:
            print("O assento já está livre.")
    else:
        print("Assento inválido!")

op = ""
while op != "4":
    print("\n1. Mostrar Assentos\n2. Reservar Assento\n3. Cancelar Reserva\n4. Sair")
    op = input("Opção: ")
    if op == "1":
        mostrar_assentos(assentos)
    elif op == "2":
        reservar(assentos)
    elif op == "3":
        cancelar(assentos)