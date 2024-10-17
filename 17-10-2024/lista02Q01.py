print("Insira 4 notas para calcular a média aritimética")

nota1 = float(input("digite a primeira nota: "))
nota2 = float(input("digite a segunda nota: "))
nota3 = float(input("digite a terceira nota: "))
nota4 = float(input("digite a quarta nota: "))
media = (nota1+nota2+nota3+nota4)/4
print("A média arimtimética entre", nota1,",",nota2,",",nota3,"e",nota4,"é: ", format(media, ".1f"))

if media >= 7:
    print("Aluno aprovado!")
else:
    print("Aluno reprovado!")
