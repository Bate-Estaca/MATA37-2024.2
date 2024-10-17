idade = int(input("Informe a idade: "))

if idade > 4 & idade <8:
    print("O nadador é da classe Infantil A")
elif idade > 7 & idade <11:
    print("O nadador é da classe Infantil B")
elif idade > 10 & idade < 14:
    print("O nadador é da classe Juvenil A")
elif idade > 13 & idade < 18:
    print("O nadador é da classe Juvenil B")
elif idade >= 18:
    print("O nadador é da classe Sênior")
else:
    print("O nadador não está apto a uma classificação")
