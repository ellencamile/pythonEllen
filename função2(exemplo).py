def calculaImposto(sal):
    novoSalario = sal - (sal*0.2)
    #print(f"O seu salario bruto é R${sal} com 20% de imposto fica {novoSalario}")
    return novoSalario
salario = float(input("Informe seu salário: "))

print(f"seu salario liquido é : R${calculaImposto(salario)}")
