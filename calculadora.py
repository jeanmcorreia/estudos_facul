print("Calculadora Simples")

resultado = 0
operacao_atual = None

while True:
    print("\nEscolha uma operação:")
    print("a. Adição")
    print("s. Subtração")
    print("m. Multiplicação")
    print("d. Divisão")
    print("r. Exibir Resultado Atual")
    print("e. Sair")

    escolha = input("Digite o número da operação (a/s/m/d/r/e): ").lower()

    if escolha in ['a', 's', 'm', 'd']:
        if operacao_atual is None:
            resultado = float(input("Digite o primeiro número: "))
        
        if escolha == 'a':
            num = float(input("Digite o número a ser adicionado: "))
            resultado += num
            operacao_atual = 'adição'
        elif escolha == 's':
            num = float(input("Digite o número a ser subtraído: "))
            resultado -= num
            operacao_atual = 'subtração'
        elif escolha == 'm':
            num = float(input("Digite o número a ser multiplicado: "))
            resultado *= num
            operacao_atual = 'multiplicação'
        elif escolha == 'd':
            num = float(input("Digite o número a ser dividido: "))
            if num != 0:
                resultado /= num
                operacao_atual = 'divisão'
            else:
                print("Erro: Divisão por zero não permitida.")
        
    elif escolha == 'r':
        print(f"Resultado Atual: {resultado}")

    elif escolha == 'e':
        print(f'Resultado final {resultado}')
        print("Saindo...")
        break

    else:
        print("Escolha inválida! Por favor, escolha uma operação (a/s/m/d/r/e).")
