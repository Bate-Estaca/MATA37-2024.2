cod = int(input("Insira o codigo: "))
quant = int(input("Insira a quantidade: "))
preco = 0

if cod == 100:
    preco = 2.50
elif cod == 101:
    preco = 4
elif cod == 102:
    preco = 10
elif cod == 103:
    preco = 12
elif cod == 104:
    preco = 4
elif cod == 105:
    preco =3.50
elif cod == 106:
    preco = 3
else:
   print("Código inválido!")
print("Valor a ser pago:",preco*quant)
