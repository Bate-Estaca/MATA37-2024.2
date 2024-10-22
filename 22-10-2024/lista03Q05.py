nota1 = int(input("Insira a primeira nota: "))
nota2 = int(input("Insira a segunda nota: "))
nota3 = int(input("Insira a terceira nota: "))

mediaPonderada = int((1*nota1 + 1*nota2 + 2*nota3)/4)

if(mediaPonderada >= 60):
    print("Aluno aprovado com média: ", mediaPonderada)
else:
    print("Aluno reprovado com média: ", mediaPonderada)
