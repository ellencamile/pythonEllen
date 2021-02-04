from datetime import date

anoA = date.today().year

while True:
    nascimento = int(input("Informe o ano do seu nascimento: "))

    idade = anoA - nascimento

    if idade >= 18:
        print(f"Você possui {idade} anos, prossiga com a inscrição")
        break
    else:
        print(f"Você possui {idade} anos, você ainda não pode se inscrever")