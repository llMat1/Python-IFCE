i = 1

while i <= 50:
    if i % 4 == 0 and i % 6 == 0:
        print("QuadHex")
    elif i % 4 == 0:
        print("Quad")
    elif i % 6 == 0:
        print("Hex")
    else:
        print(i)
    i += 1