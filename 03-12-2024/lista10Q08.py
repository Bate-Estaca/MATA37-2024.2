[produto, preco] = input().split()
preco = float(preco)
desconto = preco/10
print(f"Produto:\t{produto}\nPreço:\t\t{preco}\nDesconto:\t{desconto}\nValor a pagar:\t{preco-desconto:.2f}")
