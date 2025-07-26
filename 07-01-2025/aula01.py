v = [1, 2, 3, 4,5,6,7,8,9,10,11,12]
elem = 4
resultado = -1
middle = int(len(v)/2)


while True:
    if elem == v[middle]:
        resultado = middle
        break

    elif elem < v[middle]:
        middle = int(len(v[0:middle]))

    else:
        middle = middle +  int(len(v[middle + 1:])/2)


        


        
