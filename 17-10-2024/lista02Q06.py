print("Qual o animal?\nOBS: responda com \"s\" para sim ou \"n\" para não\n\n")

if(input("O animal é um Mamífero?\n") == "s"):
    if(input("O animal é quadrúpede?\n") == "s"):
        if(input("O animal é carnívoro?\n") == "s"):
            print("O animal é o Leão!")
        else:
            print("O animal é o Cavalo!")

    elif(input("O animal é bípede?\n") == "s"):
        if(input("O animal é onívoro?\n") == "s"):
            print("O animal é o Homem!")
        else:
            print("O animal é o Macaco!")

    elif(input("O animal é voador?\n") == "s"):
        print("O animal é o Morcego!")

    else:
        print("O animal é a Baleia!")

elif(input("O animal é uma Ave?\n") == "s"):
    if(input("O animal voa?\n") == "s"):
        if(input("O animal nada?\n") == "s"):
            print("O animal é o Pato!")
        else:
            print("O animal é a Águia!")
    else:
        if(input("O animal é tropical?\n") == "s"):
            print("O animal é o Avestruz!")
        else:
            print("O animal é o Pinguim!")


else:
    if(input("O animal tem casco?\n") == "s"):
        print("O animal é a Tartaruga!")
    elif(input("O animal tem patas?\n") == "s"):
        print(" O animal é o Crocodilo!")
    else:
        print("O animal é a Cobra!")
