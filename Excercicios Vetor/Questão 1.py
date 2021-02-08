temp = []
mes = ("Janeiro","Fevereiro","Março","Abril","Maio","Junho","julho","Agosto","Setembro","Outubro","Novembro","Dezembro")
media = 0

for cont in range(1,13):
    temp.append(float(input(f"Informe a temperatura do mês {cont}: ")))

media = sum(temp)/cont

for indice,cont in enumerate (temp):
    if cont > media:
        print(f"{mes[indice]:.<10}: {cont}")