def verificacaoNumero(numero): 
    if numero > 0:
        return 'P'
    elif numero < 0:
        return 'N'

while True:
    try:
        x = int(input("Digite um número: "))
        break
    except ValueError:
        print("Digite um número válido.")

print(verificacaoNumero(x))