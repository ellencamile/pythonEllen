from datetime import date
class Pessoa: 
    # atributo
    nome = "José"
    idade = 45
    altura = 1.65

    #metodo
    def falar(self, texto):
      print(texto)

    def comer(self):
        pass
    def calculaAno(self, idade):
        anoA = date.today().year
        print(f"Você nasceu no ano de {anoA - idade}")
# criando um objeto
alguem = Pessoa()

print(alguem.nome)
alguem.falar("To vivo")
alguem.calculaAno(alguem.idade)

#criando outro objeto 

fulano = Pessoa()
fulano.nome = "Joana"
print(fulano.nome)
fulano.calculaAno(19)