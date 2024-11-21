from random import randint
numeros=[]
pares = []
impares = []


for n in range(20):
    num = randint(0,1000)
    numeros.append(num)

    if num % 2 == 0:
        pares.append(num)
    else:
        impares.append(num)

print("Números:",numeros)
print("Pares:",pares)
print("Impares:",impares)
