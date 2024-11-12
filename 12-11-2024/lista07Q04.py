def convert24to12(hh,mm):
    AM_PM = "A"
    f_hh = hh
    if hh > 12:
        AM_PM = "P"
        f_hh = hh - 12

    printOut(f_hh, mm, AM_PM)

def printOut(hh,mm,AM_PM):
    if AM_PM == "A":
        timeEnd = "A.M"
    else:
        timeEnd = "P.M"

    print(f"{hh}:{mm} {timeEnd}")


while(True):
    hh = int(input("Insira as horas: "))
    mm = int(input("Insira os minutos: "))
    print("\n")
    convert24to12(hh,mm)
    print("\n")
    keepGoing = input("Deseja continuar? (s/n)")

    if  (keepGoing == "n") | (keepGoing == "N"):
        break
