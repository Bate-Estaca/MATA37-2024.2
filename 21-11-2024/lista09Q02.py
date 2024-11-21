from random import random
_list = []

for n in range(10):
    _list.append(random()*1000)

_list.sort(reverse=True)
print(_list)
