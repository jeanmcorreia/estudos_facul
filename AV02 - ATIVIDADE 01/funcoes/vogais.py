def contadorvogais(palavra):
    vogais = 0
    for letra in palavra:
        if letra in ['a', 'e', 'i', 'o', 'u']:
            vogais += 1
    return vogais

userInput = input("Digite uma palavra: ").lower()
print(contadorvogais(userInput))