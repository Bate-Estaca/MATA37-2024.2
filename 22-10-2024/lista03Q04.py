salario = float(input("Insira o salário: "))
prestacao = int(input("Insira o valor da prestação: "))

if(prestacao > (salario*0.2) ):
    print("Empréstimo não concedido!")
else:
    print("Empréstimo concedido!")
