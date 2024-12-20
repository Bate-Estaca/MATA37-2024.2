tabela = [
            [1200,3500,3480],
            [3226,6475,2280],
            [2118,1596,3648]
        ]
custo = [150,320,490]

maiorQnt=0
maiorArmz=0

for n in range(len(tabela)):
    qnt = sum(tabela[n])
    custoTotal = 0 #sum
    print([tabela[n][index]*custo[index] for index in range(len(tabela[n]))])
    qnt3 = tabela[n][2]
    if qnt3 > maiorQnt:
         maiorQnt  = qnt3
         maiorArmz = n

    print(f"Estoque Armaz. {n+1}:")
    print(f"Produto 1: {tabela[n][0]}    Produto 2: {tabela[n][1]}    Produto 3: {tabela[n][2]}    Total:{qnt}")

    print(f"\nCustos Armaz. {n+1}:")
    print(f"Produto 1: {tabela[n][0] * custo[0]}    Produto 2: {tabela[n][1] * custo[1]}    Produto 3: {tabela[n][2] * custo[2]}")
    print("\n")
print()
print(f"O Armazém com maior quantidade de produtos tipo 3 é o Armaz. {maiorArmz} com {maiorQnt} produtos")
