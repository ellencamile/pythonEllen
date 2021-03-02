class Funcionario:
    #Criando o metodo construtor
    def __init__(self,nome, cargo, salario = 1100):
        self.nome = nome
        self.funcao = cargo
        self.sal = salario    

    #Metodos

    def relatorio(self):
        print(f"{self.nome} é {self.funcao} e ganha {self.sal}")

fulano = Funcionario("Roberto", "Padeiro", 1100)
#fulano.relatorio()