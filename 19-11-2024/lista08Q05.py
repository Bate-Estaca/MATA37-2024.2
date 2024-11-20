def has_duplicated(_list):
    copy = _list[:]
    while len(copy) > 0:
        toSearch = copy.pop(0)
        if toSearch in copy:
            return True
    return False

_list = [1,2,3,4,5,5]

print(has_duplicated(_list))
print(_list)
