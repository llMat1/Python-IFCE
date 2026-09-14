total_primos = 0

for num in range(2, 201):
    eh_primo = True
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            eh_primo = False
            break
    if eh_primo:
        total_primos += 1

print(f"A quantidade de números primos de 1 a 200 é: {total_primos}")