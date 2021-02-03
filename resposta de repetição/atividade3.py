import time
import os
totalpessoas = int(input("Serão dadas boas vindas para quantas pessoas?"))

#CONTADORES
homem = 0
mulheres = 0

for cont in range(1, totalpessoas + 1):
    nome = input("Qual seu nome? ")
    sexo = input("Qual seu sexo m/f? ")

    if sexo == "m":
        print(f"Bem vindo sr. {nome}")
        homem += 1
    else:
        print(f"Bem vinda Sra. {nome}")
        mulheres += 1
    time.sleep(1) #espera 1 segundo
    os.system("cls") #limpa tela

print(f"Houve um total de {homem} homens e {mulheres} mulheres")