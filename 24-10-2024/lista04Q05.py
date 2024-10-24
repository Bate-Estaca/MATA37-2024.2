somaIdades=0
pessoas=0

while(True):
    idade = int(input("Insira a idade: "))
    if idade > 17:
        somaIdades += idade
        pessoas += 1
    if(input("Quer adicionar mais idades?(s/n)") == "s"):
        continue
    print()
    if pessoas == 0:
        print("Não há maiores de idade para calcular!")
    else:
        print("A soma das idades (das pessoas maiores de idade) é:", somaIdades,"\nA média das idades (das pessoas maiores de idade) é:",format(somaIdades/pessoas,".0f"))
    break

        
