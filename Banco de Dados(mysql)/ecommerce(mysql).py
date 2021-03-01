import pymysql

conexao = pymysql.connect(
    host = 'localhost',
    user = 'root',
    password = '',
    database = 'ecommerce',
)

cod = int(input("Informe o codigo do produto: "))
nome = str(input("Informe o nome do produto: ")).lower()
descricao = str(input("Informe a descrição do produto: ")).lower()
valor = float(input("Informe o valor do produto: "))

comando = "insert into produto values(%s,%s,%s,%s)"

valores = (cod,nome,descricao,valor)

consulta = conexao.cursor()

consulta.execute(comando,valores)

conexao.commit()

consulta = conexao.cursor() # a função cursor é importante pois permite interagir com o banco de dados

sql = "select * from produto"

consulta.execute(sql)

#for itens in consulta:
    #print(itens)

# exibir consulta personalisada

resultado = consulta.fetchall()

for itens in resultado:
    print(f"No mercado tem: {itens[2]} ")

conexao.close() #encerrando a conexão