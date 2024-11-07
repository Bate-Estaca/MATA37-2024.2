def nota(x):
    if x == 10:
        return "A"
    elif x >= 8:
        return "B"
    elif x >= 6:
        return "C"
    elif x >= 4:
        return "D"
    elif x >= 2:
        return "E"
    else:
        return "F"

print(nota(float(input("digite a nota: "))))
