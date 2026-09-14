idade = int(input("Digite a idade: "))

if idade >= 60:
    print("idoso")
elif idade >= 18:
    print("adulto")
elif idade >= 12:
    print("adolescente")
else:
    print("criança")