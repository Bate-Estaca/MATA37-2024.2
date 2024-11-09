def analise(n):
    pessoas=0
    maior_salario=0
    salario_350=0
    soma_salarios=0
    soma_filhos=0
    while(pessoas < n):

        salario = float(input("Insira o salário: "))
        soma_salarios += salario
        if salario > maior_salario:
            maior_salario = salario
        if salario <= 350:
            salario_350 +=1

        filhos = int(input("Insira o número de filhos: "))
        soma_filhos += filhos

        pessoas += 1

    return soma_salarios/n,soma_filhos/n,maior_salario,(salario_350/n)*100

print(analise(5))
