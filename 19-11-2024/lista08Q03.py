def chop(_list):
    del _list[len(_list) - 1]
    del _list[0]
    return None
t = [1,2,3,4]

print(chop(t))
print(t)
