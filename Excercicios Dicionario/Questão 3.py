from os import system
from time import sleep

contato = {}
listaC = []

while True:
    system("cls")
    print(f"{'Agenda':^20}")

    for itens in listaC:
        for chave, valor in itens.items():
            print(f"{chave}:{valor}")


    print("1. Inserir um contato")
    print("2. Excluir um contato")
    print("3. Sair")
    op = int(input("Qual sua escolha? "))

    if op == 3:
        break
    elif op == 1:
        nome = str(input("Informe o nome do contato: ")).title()
        fone = int(input("Informe somente o número do contato: "))

        contato[nome] = fone #a chave sera o nome do contato e o valor sera seu telefone
        listaC.append(contato.copy())

        contato.clear()
    elif op == 2:
        escolha = str(input("Informe o nome da pessoa que deseja excluir: ")).title()
        for itens in listaC:
            if escolha in itens.keys():
                itens.pop(escolha)
            else:
                print("Esse contato não existe, tente de novo")
                sleep(3)

print("="*40)