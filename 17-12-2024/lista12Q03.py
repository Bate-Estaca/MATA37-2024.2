from random import randrange

questionario = []
respostasQnt = []

#Preenche a matriz
for n in range(10):
 respostasQnt.append([])
 for m in range(5):
     respostasQnt[n].append(0)


#Gera um questionário com inserts pseudo-aleatório
#Preenche a matriz de quantidade de respostas
for n in range(int(input("Insira o número de participantes: "))):
    respostas:list[str|int] = [f"nome{n}"]
    for m in range(10):
        resposta = randrange(1,6)
        respostasQnt[m][resposta-1] += 1
        respostas.append(resposta)
    questionario.append(respostas)
questionario.append(["Vazio"] + [0]*10)


#Imprime os dados
for participante in questionario:
    if(participante[0] == "Vazio"):
        break
    print("Respostas de:",participante[0])
    for m in range(len(participante)-1):
        print (f"Pergunta {m+1}: {participante[m+1]}")
    print("\n")

print("\n")

#Imprime a relação das respostas
for numPergunta in range(len(respostasQnt)):
    print(f"Pergunta número {numPergunta+1}:")
    for numResposta in range(len(respostasQnt[numPergunta])):
        print(f"Responderam com a opção {numResposta + 1}: {respostasQnt[numPergunta][numResposta]}")
    print()


