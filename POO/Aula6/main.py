from heranca import Pessoa, Aluno, Professor

#Instaciando objeto

p1 = Pessoa("Joaquim", 54)
a1 = Aluno("Patricia", 20)
prof1 = Professor("Pertuliano", 40)

print(f"Aluno: {a1.nome}")
print(f"Professor: {prof1.nome}")
print(f"Pessoa: {p1.nome}")

p1.mostraClasse()
a1.mostraAluno()
prof1.mostraProfesor()