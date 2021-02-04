cont = 1
soma = 0 
contN = 0

while cont <= 10:
    valor = int(input(f"Informe o {cont}° valor: "))

    if valor < 0:
        contN += 1

    else:
        soma += valor
    cont += 1

print(f"A soma dos valores ositivos é {soma}")
print(f"A soma dos valores negativos é {contN}")