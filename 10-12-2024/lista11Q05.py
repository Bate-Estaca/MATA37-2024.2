from random import randrange 

primeiro_nome = ["Lucas", "João Pedro", "Maria", "Fernanda", "Luciana", "Rafael", "Igor", "Cauê", "Julia", "Roberta"]
segundo_nome = ["Silva","Bittencourt", "Almeida", "Conceissão", "Fernandes", "de Souza", "Albuquerque", "Magalhães", "Pereira"]
agenda = {}

for n in range(int(input("Defina o número de entradas: "))):
    cpf = ""
    telefone = ""
    for m in range(11):
        cpf += str(randrange(0,10))
    for m in range(9):
        telefone += str(randrange(0,10))

    agenda[cpf]={
            "nome":f"{primeiro_nome[randrange(0,len(primeiro_nome))]} {segundo_nome[randrange(0,len(segundo_nome))]} {segundo_nome[randrange(0,len(segundo_nome))]}",
            "idade": randrange(1,120),
            "telefone": telefone.replace(telefone[5], f"-{telefone[5]}",1)

            }

for key in agenda:
    print(f"{key}: {agenda[key]['nome']}-{agenda[key]['idade']}-{agenda[key]['telefone']}")

