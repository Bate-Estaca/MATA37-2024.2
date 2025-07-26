
from random import randrange ,choice

primeiro_nome = ["Maria", "Fernanda", "Luciana", "Julia", "Roberta", "Ana",  "Maria", "Luiza", "Beatriz",  "Carolina",  "Juliana", "Isabela",  "Camila", "Larissa", "Fernanda",  "Amanda",  "Letícia", "Patrícia",  "Tatiana", "Renata", "Aline",  "Sandra",  "Valeria",  "Daniela",  "Michele"]

segundo_nome = ["Silva","Bittencourt", "Almeida", "Conceissão", "Fernandes", "de Souza", "Albuquerque", "Magalhães", "Pereira","Santos", "Oliveira", "Souza", "Rodrigues", "Ferreira", "Alves", "Lima", "Gomes", "Costa", "Ribeiro", "Martins", "Carvalho", "Araújo", "Melo", "Barbosa", "Nascimento", "Lopes", "Cardoso", "Rocha", "Teixeira", "Dias", "Castro", "Moraes", "Mendonça", "Campos", "Machado", "Nogueira", "Soares", "Vieira", "Paiva", "Correia", "Pinto", "Motta", "Siqueira", "Borges", "Farias" ]

mulheres = []
maiorAltura             =0
segundaMaiorAltura      =0
maiorAlturaQnt          =0
segundaMaiorAlturaQnt   =0


for n in range(int(input("Defina o número de entradas: "))):
   mulheres.append([
       f"{choice(primeiro_nome)} {choice(segundo_nome)} {choice(segundo_nome)}",
       randrange(1,120)
       ])
mulheres.append(["VAZIO",0])



