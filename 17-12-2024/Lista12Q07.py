from random import randrange

notes   = ["péssimo","ruim","regular","bom","ótimo"]
answers = []

for n in range(100):
    answers.append([randrange(6,90),randrange(0,5)])

#• A quantidade de respostas ótimo
#• A diferença percentual entre respostas bom e regular
#• A média de idade das pessoas que responderam ruim
#• A percentagem de respostas péssimo e a maior idade que utilizou esta opção
#• A diferença de idade entre a maior idade que respondeu ótimo e a maior idade que respondeu ruim
great            = 0
good             = 0
mid              = 0
badAgeSum        = 0
badAgeAmount     = 0
terrible         = 0
mostAgedTerrible = 0
mostAgedGreat    = 0
mostAgedBad      = 0


for answer in answers:
    match(answer[1]):
        case 0:
            terrible += 1
            if answer[0] > mostAgedTerrible:
                mostAgedTerrible = answer[0]
        case 1:
            badAgeAmount += 1
            badAgeSum += answer[0]
            
            if answer[0] > mostAgedBad:
                mostAgedBad = answer[0]
        case 2:
            mid += 1
        case 3:
            good += 1
        case 4:
            great += 1

            if answer[0] > mostAgedGreat:
                mostAgedGreat = answer[0]

print(f"A quantidade de pessoas que responderam \"Ótimo\" foi de {great}")
print(f"A diferença percentual entre \"Bom\" e \"Regular\" é de {abs(good-mid)}%")
print(f"A média da idade de pessoas que responderam \"Ruim\" foi {int(badAgeSum/badAgeAmount)}")
print(f"A porcentagem de pessoas que responderam \"Péssimo\" foi de {terrible}%")
print(f"A maior idade de quem respondeu \"Péssimo\" foi {mostAgedTerrible} anos")
print(f"A diferença entre a maior idade que respondeu \"Bom\" e quem respondeu \"Ruim\" foi de {abs(mostAgedGreat - mostAgedBad)} anos")
