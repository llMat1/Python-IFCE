hora_atual = int(input("Digite a hora atual (0 a 23): "))
horas_espera = int(input("Digite a quantidade de horas para esperar: "))

hora_alarme = (hora_atual + horas_espera) % 24
print(f"O alarme irá tocar às {hora_alarme} horas.")