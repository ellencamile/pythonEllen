from heranca2 import  Aluno, Professor

a1 = Aluno("Matilda", 23, 987)

a1.mostraAluno()

print(f"A matricula de {a1.nome} é {a1.matricula}")

prof1 = Professor("Petulio", 54, 3100)

prof1.mostraProfesor()

print(f"O salario do {prof1.nome} é {prof1.salario}")