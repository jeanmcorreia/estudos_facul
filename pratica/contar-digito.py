def contarDigitos(numero):
    return len(str(abs(numero)))

while True:
    try:
        x = int(input("Digite um número: "))
        break
    except ValueError:
        print("Digite um número válido.")

print(contarDigitos(x))