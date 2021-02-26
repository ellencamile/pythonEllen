import pymysql

# Estabelecer a conexão
conexao = pymysql.connect(
    host = 'localhost',
    user = 'root',
    password = '',
    database = 'turma_sistema'
)

consulta = conexao.cursor() # a função cursor é importante pois permite interagir com o banco de dados

sql = "select * from aluno"

consulta.execute(sql)

#for itens in consulta:
    #print(itens)

# exibir consulta personalisada

resultado = consulta.fetchall()

for itens in resultado:
    print(f"Olá {itens[1]} você mora no bairro {itens[4]}")

conexao.close() #encerrando a conexão