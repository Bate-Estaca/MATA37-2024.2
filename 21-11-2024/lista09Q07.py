pares = 0
impares = 0

for n in range(10):
    if int(input("Digite um número:")) % 2 == 0:
        pares += 1
    else:
        impares += 1

print("Números pares:",pares)
print("Números ímpares:",impares)
