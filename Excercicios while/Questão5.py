while True:
    valor = int(input("Informe um valor inteiro: "))

    if valor < 0:
        break

    if valor > 100:
        print("LIMITE EXCEDIDO")
    elif valor> 10:
        print(f"O quadrado de valor é {valor**2}")
    elif valor > 5:
        print(f"O cubo de {valor} é {valor**3}")