while True: 
    login = str(input("Informe o seu login: "))
    senha = str(input("Informe a sua senha: "))

    if senha == login:
        print("Você não pode usar a mesma palavra em login e senha, pois não é seguro.")  
        print("Informe uma senha valida!")
    else:
        print("Você esta cadastrado, bem vindo(a)")

        break

while True:
    login2 = str(input("Informe seu login: "))
    senha2 = str(inpunt())