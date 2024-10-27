from math import gcd

distancia = int(input("Insira a distância percorrida em KM's: "))
gasolina = int(input("Insira a quantidade de gasolina consumida em Litros: "))

razao = distancia/gasolina
mdc = gcd(distancia,gasolina)
proporcao = str(distancia/mdc)+"KM/"+str(gasolina/mdc)+"L"

print("O consumo do seu carro é:",proporcao)

if razao < 8:
    print("Venda o carro!")
elif (razao >=8) & (razao <=14):
    print("Econômico")
else:
    print("Super econômico")


