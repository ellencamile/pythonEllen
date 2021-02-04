from os import system
while True: 
    login = str(input("Informe o seu login: "))
    senha = str(input("Informe a sua senha: "))

    if senha == login:
        print("Você não pode usar a mesma palavra em login e senha, pois não é seguro.")  
        print("Informe uma senha valida!")
    else:
        print("Você esta cadastrado, bem vindo(a)")
        break
system("Cls")

while True:
    login2 = str(input("Informe seu login: "))
    senha2 = str(input("Informe seu login:"))
    
    if login2 == login:
        print("Nome de usuario não esta disponivel, tente outro")
    elif login2 == senha2:
        print("Você não pode usar a mesma palavra em login e senha, pois não é seguro.")
        print("Informe uma senha válida!")
    else:
        print("Você esta cadastrado, bem vinda(a)")
        break