from funcionario import Funcionario

f1 = Funcionario("Rosangela", "Aux Cozinha", 1600)

f1.relatorio()

f2 = Funcionario("Alberto", "Pedreiro")
print(f"O salario de {f2.nome} é R$ {f2.sal}")