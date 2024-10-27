num1 = int(input("Insira um número: "))
num2 = int(input("Insira outro número: "))
num3 = int(input("Insira o ultimo número: "))

maior = num1
if num2 > maior:
    maior = num2
if num3 > maior:
    maior = num3

menor = num1
if num2 < menor:
    menor = num2
if num3 < menor:
    menor = num3
print(menor, maior)
if (num1 != menor) & (num1 != maior):
    print(menor,num1,maior)
elif (num2 != menor) & (num2 != maior):
    print(menor,num2,maior)
elif (num3 != menor) & (num3 != maior):
    print(menor,num3,maior)
else:
    print(num1,num1,num1)


