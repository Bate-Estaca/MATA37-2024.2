tabela = [
        [1200,3500,3480],
        [3226,6475,2280],
        [2118,1596,3648]
        ]
custo = [150,320,490]

maiorArmz = 0
maiorQnt = 0
for n in range(len(tabela)):
    qnt = sum(tabela[n])
    if qnt > maiorQnt:
        maiorArmz = n+1
        maiorQnt = qnt
    print(f"Armaz. {n+1}:\t{qnt}")
print(f"O Armazém com maior quantidade de produtos é o Armaz. {maiorArmz} com {maiorQnt} produtos")


