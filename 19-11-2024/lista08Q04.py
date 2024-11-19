def is_sorted(_list):
    first = _list[0]
    last = _list[len(_list) - 1 ]
    if  first ==  last or first<last :
        return True
    return False
        
print(is_sorted([4,5,3]))
