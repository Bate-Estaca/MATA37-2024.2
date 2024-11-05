import random
arr = []

for n in range(10):
    arr.append(random.randint(0,100))

even = []
odd = []

for value in arr:
    if value % 2 == 0:
        even.append(value)
    else:
        odd.append(value)

print("números:",*arr)
print("Quantidade de número pares:",len(even),"\tsão eles: ",*even)
print("Quantidade de número ímpares:",len(odd),"\tsão eles: ",*odd)

