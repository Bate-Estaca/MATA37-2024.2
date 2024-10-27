idade = int(input("Insira a idade: "))
tempoServico = int(input("Insira o tempo de serviço: "))

if (idade >=65) | (tempoServico >= 30) | ((idade >= 60) & (tempoServico >= 25)):
    print("Pode se aposentar")
else:
    print("Não pode se aposentar!")

