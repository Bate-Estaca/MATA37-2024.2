while(True):
    choice = int(input("1 - Soma\n2 - Subtração\n3 - Multiplicação\n4 - Divisão\n5 - Sair\n\nEscolha> " ))
    num1 = float(input("Digite um número: "))
    num2 = float(input("Digite outro número: "))            
    if(choice == 1):
        print("A soma entre:",num1,"e",num2,"é igual a:",num1+num2)
    elif(choice == 2):
        print("A subtração entre:",num1,"e",num2,"é igual a:",num1-num2)
    elif(choice == 3):
        print("A multiplicação entre:",num1,"e",num2,"é igual a:",num1*num2)
    elif(choice == 4):
        print("A divisão entre:",num1,"e",num2,"é igual a:",num1/num2)
    elif(choice == 5):
        break
    else:
        print("opção inválida!")
    print("\n")
