def somarlista(lista):
    total = 0
    for c in lista:
        total += c
    return total
    
qtd = int(input("Digite quantos números deseja adicionar: "))
numerosadcionados = 0
listuser = []
while numerosadcionados < qtd:
    numero = int(input("Digite um número: "))
    listuser.append(numero)
    numerosadcionados += 1

print(somarlista(listuser))