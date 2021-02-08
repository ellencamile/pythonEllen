from os import system

frutas = list()

for cont in range(1,6):
    frutas.append(input("Informe um nome de fruta: "))

while True:
    system("cls")
    print(f"{'lista de fruta':*^30}\n")

    for indice, itens in enumerate(frutas):
        print(f"{indice:.<10} {itens}")
    print("\n")
    print("0. Terminar")
    print("1. Inserir uma fruta")
    print("2. Excluir uma fruta")
    op = int(input("O que deseja fazer: "))

    if op == 0:
        break
    elif op == 1:
            frutas.append(input("Informe uma nova fruta: "))
    elif op == 2:
        valor = int(input("Qual a posição da fruta que você deseja remover? "))
        frutas.pop(valor)
print("Obrigada por usar o sistema\n\n")
