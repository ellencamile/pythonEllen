from datetime import date
anoA = date.today().year

def divisoria():
    print("-"*50)

nome = str(input("Informe seu nome: "))
divisoria()

idade = int(input("Informe sua idade: "))
divisoria()

print(f"Ola {nome} você nasceu no ano de: {anoA - idade}")
divisoria()