def medialista(lista):
    total = 0
    qtd_numeros = len(lista)
    for c in lista:
        total += c
    return total / qtd_numeros
    
qtd = int(input("Digite quantos números deseja adicionar: "))
numerosadicionados = 0
listuser = []
while numerosadicionados < qtd:
    numero = float(input("Digite um número: "))
    listuser.append(numero)
    numerosadicionados += 1

print(medialista(listuser))