'''
texto = "faz por ti e eu te ajudarei"

print("tu" in texto)
'''

for cont in range(1,11):
    print(cont," ",end="") #impedindo de quebrar linha

for cont in range(1,21,2): # o 3º parâmetro é incremento dos valores
    print(cont)

for cont in range(11,0,-1):
    print(cont," ", end="") #decrementando os valores
print("\n\n")
print("-"*15,"VALORES PARES","-"*15)
for cont in range(1,11):
    if cont %2 ==0:
        print(cont, " ")