arr = []

arr.append(float(input("Insira um número: ")))

times = 4

for value in range(1,5):
    arr.append(float(input("Insira outro número: ")))

maior = 0
for value in arr:
    if value > maior:
        maior=value

print(maior)

