def cadastrar_despesa(despesas: list) -> None:
    data = input("Data (DD/MM/AAAA): ")
    descricao = input("Descrição: ")
    valor = float(input("Valor: R$ "))
    despesas.append([data, descricao, valor])

def listar_despesas(despesas: list) -> None:
    print("\n--- Despesas ---")
    for d in despesas:
        print(f"Data: {d[0]} | Descrição: {d[1]} | Valor: R$ {d[2]:.2f}")

def calcular_total(despesas: list) -> None:
    total = 0.0
    for d in despesas:
        total += d[2]
    print(f"\nValor total gasto: R$ {total:.2f}")

lista_despesas = []
op = ""
while op != "4":
    print("\n1. Cadastrar Despesa\n2. Listar Despesas\n3. Calcular Total\n4. Sair")
    op = input("Opção: ")
    if op == "1":
        cadastrar_despesa(lista_despesas)
    elif op == "2":
        listar_despesas(lista_despesas)
    elif op == "3":
        calcular_total(lista_despesas)