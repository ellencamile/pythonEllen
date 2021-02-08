from os import system

numeros = []

for cont in range(1,11):
    numeros.append(int(input(f"Imforme o valor {cont}: ")))

system("cls")

for indice,cont in enumerate(numeros):
    print(f"{indice:-<10}>{cont}")

pos1= int(input("Escolha a 1ª posicão: "))
pos2= int(input("EScolha a 2ª posicão: "))

print(f"{numeros[pos1]} x {numeros[pos2]} = {numeros[pos1] * numeros[pos2]}")
print(f"{numeros[pos1]} + {numeros[pos2]} = {numeros[pos1] + numeros[pos2]}")
print(f"{numeros[pos1]} - {numeros[pos2]} = {numeros[pos1] - numeros[pos2]}")
print(f"{numeros[pos1]} / {numeros[pos2]} = {numeros[pos1] / numeros[pos2]}")
print(f"{numeros[pos1]} ** {numeros[pos2]} = {numeros[pos1] ** numeros[pos2]}")