from random import randrange ,choice

primeiro_nome = ["Lucas", "João Pedro", "Maria", "Fernanda", "Luciana", "Rafael", "Igor", "Cauê", "Julia", "Roberta"]
segundo_nome = ["Silva","Bittencourt", "Almeida", "Conceissão", "Fernandes", "de Souza", "Albuquerque", "Magalhães", "Pereira"]
DDDs = [11,12,13,14,15,16,17,18,19,21,22,24,27,28,31,32,33,34,35,37,38,41,42,43,44,45,46,47,48,49,51,53,54,55,61,62,63,64,65,66,67,68,69,71,73,74,75,77,79,81,82,83,84,85,86,87,88,89,91,92,93,94,95,96,97,98,99]
agenda = {}


for n in range(int(input("Defina o número de entradas: "))):
    cpf = ""
    telefone = ""
    for m in range(11):
        cpf += str(randrange(0,10))
    for m in range(8):
        telefone += str(randrange(0,10))

    
    agenda[cpf]={
            "nome":f"{choice(primeiro_nome)} {choice(segundo_nome)} {choice(segundo_nome)}",
            "idade": randrange(1,120),
            "telefone": "+55(" + str(choice(DDDs)) + ")9" + telefone[0:4] + "-" + telefone[4:8]
            }

for key in agenda:
    print(f"{key}: {agenda[key]['nome']}-{agenda[key]['idade']}-{agenda[key]['telefone']}")

