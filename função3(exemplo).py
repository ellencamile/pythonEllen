def calculaImposto(sal, imposto = False):
   '''
   Funcão que calcula o imposto de um funcionario
   \nsal: parametro que recebe o salario do funcionario
   \nimposto: parametro opcional que permite mudar o valor do imposto
   '''
    if imposto:
        desconto = float(input("Qual a porcentagem do imposto: "))
    else:
        desconto = 20
    desconto = desconto/100

    return sal - (sal *desconto)

salario = float(input("Informe seu salario: "))

print(f"Seu salário com desconto é: R${calculaImposto(salario)}")