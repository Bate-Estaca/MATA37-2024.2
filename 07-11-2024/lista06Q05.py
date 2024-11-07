def categoria(idade):
    if idade >= 18:
        return "Adulto"
    elif idade >= 14:
        return "Juvenil B"
    elif idade >= 11:
        return "Juvenil A"
    elif idade >= 8:
        return "Infantil B"
    elif idade >= 5:
        return "Infantil A"
    else:
        return "Não está apto a classificação"


print(categoria(int(input("digite a idade: "))))
