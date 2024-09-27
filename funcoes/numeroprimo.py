def numeroprimo(numero):
    if numero == 2 or numero % 2 != 0:
        return True
    elif numero % 2 == 0:
        return False
    
numUsuario = int(input("Digite um número: "))
print(numeroprimo(numUsuario))