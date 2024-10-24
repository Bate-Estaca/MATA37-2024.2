maiorAltura = 0
menorAltura = 0
pessoas = 0

while pessoas < 5:
    pessoas += 1
    altura = float(input("Informe a altura: "))

    if menorAltura == 0:
            menorAltura = altura

    if altura > maiorAltura:
        maiorAltura = altura
    if altura < menorAltura:
        menorAltura = altura
print("A menor altura foi:",format(menorAltura, ".2f"), "\nA maior altura foi:", format(maiorAltura, ".2f"))
