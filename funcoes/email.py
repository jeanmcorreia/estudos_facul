def ehemail(email):
    for caracter in email:
        if caracter == '@':
            return "Possui @"
    return "Não possui @"

def regexemail(email):
    
emailUser = input("Digite o email: ")
print(ehemail(emailUser))