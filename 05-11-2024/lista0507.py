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
print("pares:",*even)
print("ímpares",*odd)

