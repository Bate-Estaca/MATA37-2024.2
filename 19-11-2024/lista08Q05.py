def has_duplicated(_list):
    copy = _list
    while len(copy) > 0:
        toSearch = copy.pop(0)
        if toSearch in copy:
            return True
    return False


print(has_duplicated([1,2,3]))
print(has_duplicated([1,2,2]))
print(has_duplicated([3,2,3]))
