perguntas =["Telefonou para a vítima?","Esteve no local do crime?","Mora perto da vítima?","Devia para a vítima?","Já trabalhou com a vítima?"]

participacao = 0

while(input("Responda as próximas perguntas com \"s\" para sim e \"n\" para não\nEntendeu? ") != "s"):
    print()

index = 0
while index < len(perguntas):
    print()
    print(perguntas[index])
    resposta = input("Resposta: ")
    if  resposta == "s":
        participacao += 1
        index += 1
    elif resposta == "n":
        index += 1
    else:
        print("\nResposta inválida!\n")
        
print("Classificação: ",end=" ")
if participacao == 2:
    print("Suspeito")
elif participacao >2 and participacao < 5:
    print("Cúmplice")
elif participacao == 5:
    print("Assassino")
else:
    print("Inocente")

