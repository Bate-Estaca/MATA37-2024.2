from random import randrange,random

store = []

for n in range(100):
    store.append([randrange(0,80),round(random() * 18.75 + 2,2)])

billing = 0
for id in range(len(store)):
    billing += store[id][0] * store[id][1]

print(f"O faturamento foi de R${billing:.2f}")
