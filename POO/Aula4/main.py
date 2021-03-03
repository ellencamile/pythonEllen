from associacao import Celular, Pessoa

smartphone = Celular("Xiaomi", 1500)

p1 = Pessoa("Jeruza", 45, "Rua 71")

print(f"{p1.nome} mora no endereço {p1.endereco} e tem {p1.idade} anos")

p1.celular = smartphone

print(f"{p1.nome} possui um celular da marca {p1.celular.marca} e custou {p1.celular.valor}")