from random import random

carros = ["Fusca", "Kwid", "Gol ","Ranger", "Jeep"]
kmL = [round(random()*17 + 3,2),round(random()*17 + 3,2),round(random()*17 + 3,2),round(random()*17 + 3,2),round(random()*17 + 3,2)]

print("Comparativo de consumo de combustível")
print()

for index in range(len(carros)):
    print(f"Veículo {index + 1}\nNome: {carros[index]}\nKm por litro: {format(kmL[index],".2f")}\n")



print("Relatório Final")

for index in range(len(carros)):
    litros = round(1000/kmL[index],1)
    print(f"{index + 1} - {carros[index]}\t- {kmL[index]}\t- {litros} litros\t- R$ {round(litros * 2.25,2)}")

print()
maisEco = kmL.index(max(kmL))
print(f"O modelo mais econômico é o {carros[maisEco]} rodando {kmL[maisEco]} por litro")
