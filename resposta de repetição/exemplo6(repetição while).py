from os import system
system("cls")

print("="*15,"EXEMPLO 1","="*15)

valor = 1

while valor <= 10:
    print(valor)
    valor += 1

num = 0

while True: 
    num = int(input("Informe um valor: "))

    if num == 0:
        break
