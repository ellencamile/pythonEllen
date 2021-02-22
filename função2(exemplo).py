def calculaImposto(sal,imposto):
    imposto = imposto/100 #calculando a porcentagem do valor 
    novoSalario = sal - (sal*imposto)
    
    #print(f"O seu salario bruto é R${sal} com 20% de imposto fica {novoSalario}")
    
    return novoSalario

salario = float(input("Informe seu salário: "))

desconto = float(input("Qual o valor da porcentagem de imposto: "))

print(f"seu salario liquido com {desconto}% de desconto é R${calculaImposto(salario,desconto)}")
