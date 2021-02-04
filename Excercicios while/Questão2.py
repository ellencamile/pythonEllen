cont = 0
while True:
    num = int(input("Informe numeros aleatorios: "))

    if num == 0:
        break
    if cont == 0:
        maior = num
        menor = num
    else:
        if num > maior:
            maior = num
        elif num < menor:
            menor = num
    cont += 1
print(f"O maior valor é {maior} e o menor é {menor}")