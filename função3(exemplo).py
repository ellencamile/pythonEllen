def calculaImposto(sal, imposto = False):
    if imposto:
        desconto = float(input("Qual a porcentagem do imposto: "))
    else:
        desconto = 20
    desconto = desconto/100

    return sal - (sal *desconto)

salario = float(input("Informe seu salario: "))

print(f"Seu salário com desconto é: R${calculaImposto(salario)}")