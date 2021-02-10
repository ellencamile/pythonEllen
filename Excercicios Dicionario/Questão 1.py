alunos = dict()
turma = list()

for cont in range(0,5):
    alunos['nome'] = str(input("Informe o nome do aluno: ")).title()
    alunos['nota1'] = float(input(f"Informe a nota 1 de {alunos['nome']}: "))
    alunos['nota2'] = float(input(f"Informe a nota 2 de {alunos['nome']}: "))
    alunos['nota3'] = float(input(f"Informe a nota 3 de {alunos['nome']}: "))
    alunos['media'] = (alunos['nota1'] + alunos['nota2'] + alunos['nota3'])/3

    turma.append(alunos.copy())
    alunos.clear() #limpando a dicionario

print("\n",turma,"\n")


for itens in turma:
    for chave, valor in itens.items():
        if chave == "nome":
            print(f"aluno(a) {valor}")

        if chave == "media":
            print(f"Teve media = {valor:.2f}")