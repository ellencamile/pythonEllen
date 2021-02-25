import pymysql

conexao = pymysql.connect(
    host = 'localhost',
    user = 'root',
    password = '',
    database = 'turma_sistema'
)

consulta = conexao.cursor()

sql = "select * from disciplina where carga_horaria >= 150"

consulta.execute(sql)

resultado = consulta.fetchall()

for itens in resultado:
    print(f"O nome da disciplina é {itens[2]} e a carga horaria é {itens[3]}")