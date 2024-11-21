from random import randint

opcoes = ["Windows Server", "Unix", "Linux", "Netware", "Mac OS", "Outro"]
votos =[0,0,0,0,0,0]

#Simula o resultado da votação
votacaoResultado = [1]*randint(1,1000) + [2]*randint(1,1000) + [3]*randint(1,1000) + [4]*randint(1,1000) + [5]*randint(1,1000) + [6]*randint(1,1000) + [0]

totalVotos = 0;
voto = votacaoResultado.pop(0)
while voto != 0 :
    votos[voto - 1] += 1
    totalVotos += 1
    voto = votacaoResultado.pop(0)


print("Sistema Operacional\t\tVotos\t%")
print("-"*20,"\t\t","-"*5,"\t","-"*5,sep="")
print()

print(f"{opcoes[0]}\t\t\t{votos[0]}\t{format(votos[0]*100/totalVotos,".2f")}%\n")
for index in range(1,len(opcoes)):
    print(f"{opcoes[index]}\t\t\t\t{votos[index]}\t{format(votos[index]*100/totalVotos,".2f")}%")
    print()

print("-"*20,"\t\t","-"*5,sep="")
print("Total\t\t\t\t",totalVotos,sep="")


