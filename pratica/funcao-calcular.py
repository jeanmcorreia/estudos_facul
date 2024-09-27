def calcular(x, y, operacao):
    if operacao == 'A':
        return (x + y)
    elif operacao == 'S':
        return (x - y)
    elif operacao == 'M':
        return (x * y)
    elif operacao == 'D':
        try:
            return (x / y)
        except ZeroDivisionError:
            return "Não é possível dividir por 0"

while True:
    try:
        numero1 = float(input("Digite um número: "))
        numero2 = float(input("Digite outro número: "))
        opc = input("A - adição\nS - Subtração\nM - Multiplicar\nD - Divisão\n").upper()
        if opc not in ['A', 'S', 'M', 'D']: ##tinha colocado != porém é uma lista
            print("Digite uma operação válida.")
        else:
            break
    except ValueError:
        print("Digite valor ou operação válida.")

print(calcular(numero1, numero2, opc)) 
