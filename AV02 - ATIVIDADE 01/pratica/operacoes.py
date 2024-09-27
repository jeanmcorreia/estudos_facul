def somar(num1, num2):
    return num1+num2

def subtrair(num1, num2):
    return num1-num2

def multiplicar(num1, num2):
    return num1*num2

def dividir(num1, num2):
    try:
        return num1/num2
    except ZeroDivisionError:
        return "Não é possível dividir por 0 (zero)"


while True:
    try:
        opc = int(input("1 - ADICÃO\n2 - SUBTRAÇÃO\n3 - MULTIPLICAÇÃO\n4- DIVISÃO\nSelecione a operação desejada: "))
        if opc < 1 or opc > 4:
            print("Digite um valor inteiro de 1 a 4.")
        else:
            break
    except ValueError:
        print("Digite um valor inteiro de 1 a 4.")

while True:
    try:
        x = float(input("Digite um número: "))
        y = float(input("Digite outro número: "))
        break
    except ValueError:
        print("Digite um número válido")
if opc == 1:
    print(somar(x, y))
elif opc == 2:
    print(subtrair(x, y))
elif opc == 3:
    print(multiplicar(x, y))
elif opc == 4:
    print(dividir(x, y))