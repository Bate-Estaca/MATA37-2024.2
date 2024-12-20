from random import randrange

estados = []

for n in range(20):
    estados.append([])
    for m in range(10):
        estados[n].append(randrange(300, 1000000))

maiorPopulacao = maiorNumEstado = maiorNumCidade = mediaCapitais = 0

for numEstado in range(len(estados)):
     for numCidade in range(len(estados[numEstado])):
         if numCidade == 0:
             mediaCapitais += estados[numEstado][numCidade]
         if estados[numEstado][numCidade] > maiorPopulacao:
            maiorPopulacao = estados[numEstado][numCidade] 
            maiorNumEstado = numEstado
            maiorNumCidade = numCidade

print(f"A cidade mais populosa e´ a cidade {maiorNumCidade} do estado {maiorNumEstado}, com {maiorPopulacao} habitantes!")
print(f"A me´dia da populaça˜o das capitais e´ {int(mediaCapitais/len(estados)*len(estados[0]))}")
