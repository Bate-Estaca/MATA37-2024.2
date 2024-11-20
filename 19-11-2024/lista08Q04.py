def is_sorted(_list):
    copy = _list[:]
    copy.sort()
    if copy == _list:
        return True
    return False
        
print(is_sorted(["a","b","c"]))
