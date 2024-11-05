import random
arr = []
for n in range(5):
    arr.append(random.randint(1,100))

_sum = 0
for value in arr:
    _sum += value

print("os números de entrada foram:",*arr)
print("A soma é:",_sum,"\ta média é:",_sum/len(arr))
