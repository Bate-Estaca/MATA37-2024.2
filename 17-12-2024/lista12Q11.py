from random import randrange, random

gabarito        = []
alunos          = []
aprovados       = 0
frequenciaNotas = [0] * 11 

for n in range(10):
    gabarito.append(randrange(0,5))

for n in range(50):
    alunos.append([n,[]])
    for m in range(10):
        alunos[n][1].append(round(gabarito[m] + random() - 0.2))



for aluno in alunos:
    nota = 0;

    for indexResposta in range(len(aluno[1])):
        if aluno[1][indexResposta] == gabarito[indexResposta]:
            nota += 1.0

    if nota >= 7:
        aprovados += 1
    frequenciaNotas[int(nota)] += 1


    print()
    print("Numero de matricula:", aluno[0])
    print("Nota:",nota)
    print()

frequenciaAbsoluta     = 0
notaFrequenciaAbsoluta = 0 
for nota in range(len(frequenciaNotas)):
    if frequenciaNotas[nota]  > frequenciaAbsoluta:
        frequenciaAbsoluta = frequenciaNotas[nota]
        notaFrequenciaAbsoluta = nota

print(f"A taxa de aprovação foi de {aprovados*100/len(alunos)}%") 
print(f"A nota com maior frequência absoluta foi a nota {notaFrequenciaAbsoluta}")

