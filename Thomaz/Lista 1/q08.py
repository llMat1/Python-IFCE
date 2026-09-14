km = float(input("Digite a distância em quilômetros: "))

metros = km * 1000
centimetros = km * 100000
milhas = km * 0.621371

print(f"{km} km equivalem a:")
print(f"- Metros: {metros:.2f} m")
print(f"- Centímetros: {centimetros:.2f} cm")
print(f"- Milhas: {milhas:.4f} mi")