num = int(input("Insira um número: "))

fatorial = num
for n in range(1, num):
    fatorial = fatorial  * (num - n)

print(fatorial)
