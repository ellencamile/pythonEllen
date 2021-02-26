from pymongo import MongoClient

#estabelecendo a conexão

cliente = MongoClient('localhost', 27017)

banco = cliente.santander #criando um banco de dados 

colecao = banco.clientes #criando collections

while True:
    print(f"{' MENU ':=^40}")
    op = int(input('''
        1. Inserir dados
        2. Exibir dados
        3. Excluir dados
        4. Sair

        Qual sua escolha: '''))

    if op == 1:
        cpf = int(input("Informe o seu cpf: "))
        nome = str(input("Informe seu nome: ")).title()
        sexo = str(input("Informe o seu sexo(f/m): ")).lower()
        sal = float(input("Informe seu salario: "))
        end = str(input("Informe seu endereço: "))

        #inserindo dados na collection
        colecao.insert_one({
            'cpf':cpf,
            'nome':f'{nome}',
            'sexo':f'{sexo}',
            'salario':sal,
            'endereco':f'{end}'
        })
        print("\nDados inseridos com sucesso!\n")
    elif op == 2:
        print(f"{'Exibindo os dados':-^30}")
        for item in colecao.find():
            print(f"{item['nome']}, possui salario de R${item['salario']}, e mora no endereço {item['endereco']} e o seu cpf é {item['cpf']}")
        
        print("-"*40)
    elif op == 3:
        escolha = int(input("Qual cpf do cliente você deseja excluir: "))
        resultado = colecao.delete_one({
            'cpf': escolha
        })
        print("Cliente excluidos: ",resultado.deleted_count) #contando quantos itens foram excluidos
    elif op == 4:
        break
    
    #break