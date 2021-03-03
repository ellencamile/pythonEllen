from agregacao import Cliente, Conta

c1 = Cliente("Pedro", "98 12345678", "123.456.789-87", "Rua do calçadão, 34, Bairro Turu")

conta1 = Conta(1234,c1,1100,2000)

print(f"{c1.nome} possui o saldo de R${conta1.saldo} e mora no endereço {c1.endereco} e possui o telefone {c1.telefone} e limite de R${conta1.limite}")

print(f"{conta1.titular.nome} possui o saldo de R${conta1.saldo} e mora no endereço {conta1.titular.endereco} e possui o telefone {conta1.titular.telefone} e limite de R${conta1.limite}")