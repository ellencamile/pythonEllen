# trabalhando com a função filter
valores = list(range(20,61))
print(valores)

pares = list(filter(lambda num:num%2==0,valores))

print("Os valores pares são: \n",pares)