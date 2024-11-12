def somaImposto(taxaImposto, custo):
    return custo + (custo * (taxaImposto/100))

taxa =  float(input("Insira a taxa do imposto sem '%': "))
custo = float(input("Insira o custo do produto: "))

print(somaImposto(taxa,custo))
