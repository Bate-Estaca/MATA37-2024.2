
num = int(input("Informe um número: "))
inicio = int(input("Insira o inicio da tabuada: "))
fim = int(input("Insira o fim da tabuada: "))

while inicio<=fim:
    print(num,"x",inicio,"=",num*inicio)
    inicio += 1
