from random import randrange,choice

habitantes = []
sexos       = ["masculino","feminino"] 
coresOlho   = ["azuis","verdes","castanhos"]
coresCabelo = ["pretos","castanhos","louros"]

maiorIdade = 0
totalFeminino = 0
habitantes111 = 0


#Gera o conteúdo da lista habitantes
for n in range(int(input("Insira o número de habitantes: "))):
    habitantes.append({"idade":randrange(0,106),"sexo":choice(sexos),"corOlhos":choice(coresOlho),"corCabelo":choice(coresCabelo)})
habitantes.append({"idade":-1,"sexo":"","corOlhos":"","corCabelo":""})

for habitante in habitantes:
    if habitante["idade"] > maiorIdade:
        maiorIdade = habitante["idade"]

    if habitante["sexo"] == "feminino":
        totalFeminino += 1

        if 18 <= habitante["idade"] <= 35       and \
           habitante["corOlhos"] == "verdes"    and \
           habitante["corCabelo"] == "castanhos":
            habitantes111 += 1

print(f"A maior idade entre os habitantes é de {maiorIdade} anos.")
print()
print(f"A porcentagem de indivíduos do sexo feminino cuja idade está entre 18 e 35 anos, que tenham olhos verdes e cabelos louros é de:")
print(f"Entre todos os habitantes: {round(habitantes111*100/len(habitantes),2)}%")
print(f"Entre os habitantes do sexo feminino: {round(habitantes111*100/totalFeminino,2)}%")

#A maior idade dos habitantes
#A porcentagem de indivíduos do sexo feminino cuja idade está entre 18 e 35 anos inclusive e que tenham olhos verdes e cabelos louros
