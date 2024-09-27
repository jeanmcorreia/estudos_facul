def contarPalavras(string):
    palavras = string.split()
    return len(palavras)

userString = input("Digite aqui: ")

print(contarPalavras(userString))