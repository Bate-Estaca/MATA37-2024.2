
print("Insira 4 notas para calcular a média aritimética")

nota1 = float(input("digite a primeira nota: "))
nota2 = float(input("digite a segunda nota: "))
nota3 = float(input("digite a terceira nota: "))
nota4 = float(input("digite a quarta nota: "))
media = (nota1+nota2+nota3+nota4)/4
print("A média arimtimética entre", nota1,",",nota2,",",nota3,"e",nota4,"é: ", format(media, ".1f"))

if (media >=3) & (media < 7):
    if(float(input("O aluno tem direito a prova final, insira sua nota: ")) < 5):
        print("aluno reprovado por conceito! (AC)")
    else:
        print("aluno aprovado por conceito (RC)")
elif media >= 7:
    print("Aluno aprovado por média! (AM)")
else:
    print("Aluno reprovado por média! (RM)")
