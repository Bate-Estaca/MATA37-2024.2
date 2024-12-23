from random import random

oxen = []

#Gera as informações dos bois
for n in range(90):
    oxen.append({"id":n,"weight":round((random()*690)+300,3)})

#Inicia as variáveis locais
fattestID      = 0
fattestWeight  = 0
thinnestID     = 0
thinnestWeight = oxen[0]["weight"]

for ox in oxen:
    if ox["weight"] > fattestWeight:
        fattestWeight = ox["weight"]
        fattestID = ox["id"]
    if ox["weight"] < thinnestWeight:
        thinnestWeight = ox["weight"]
        thinnestID = ox["id"]

print(f"O boi mais gordo é o de id {fattestID}, pesando {fattestWeight}Kg")
print(f"O boi mais magro é o de id {thinnestID}, pesando {thinnestWeight}Kg")
