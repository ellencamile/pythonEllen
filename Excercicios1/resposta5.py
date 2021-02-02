vPermitida = float(input("Qual a velocidade permitida? "))
vMotorista = float(input("Qual a velocidade do motorista? "))

#calcular 20% a mais 
vPermitida20 = (vPermitida * 0.2) + vPermitida

#calcula 50% a mais 
vPermitida50 = (vPermitida * 0.5) + vPermitida

if vMotorista <= vPermitida:
    print("Tudo certo, não precisa pagar multa")
elif vMotorista > vPermitida and vMotorista <= vPermitida20:
    print("Você cometeu infração media\nAssim irá pagar R$85.00 e recebera 4 pontos na carteira")
elif vMotorista > vPermitida20 and vMotorista <= vPermitida50:
    print("Você cometeu uma infração grave\nAssim irá pagar R$127.00 e recebera 5 pontos na carteira")
elif vMotorista > vPermitida50:
    print("Você cometeu uma infração gravissima\nAssim irá pagar R$574.00 além de receber 7 pontos na carteira\n Ter carteira apreendida e \n ter o direito de dirigir suspenso")