def fatorial(numero):
    if numero < 0:
        return "Número negativo."
    elif numero == 0:
        return 1
    else:
        return numero * fatorial(numero - 1)
    
num = int(input("Digite um número: "))
print(fatorial(num))