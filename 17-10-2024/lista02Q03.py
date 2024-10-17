ladoA = int(input("Insira um valor: "))
ladoB = int(input("Insira outro valor: "))
ladoC = int(input("Insira um último valor: "))

if(ladoA < ladoB+ladoC) & (ladoB < ladoA+ladoC) & (ladoC < ladoA+ladoB):
    print("Os três lados formam um triângulo")
    if (ladoA == ladoB) & (ladoA == ladoC):
        print("O triangulo é equilátero")
    elif (ladoA == ladoB) & (ladoA != ladoC):
        print("O triângulo é isósceles")
    else:
        print("O triângulo é escaleno")
else:
    print("Não é um triângulo")
