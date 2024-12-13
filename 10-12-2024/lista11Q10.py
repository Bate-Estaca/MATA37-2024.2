from os import system
choice = None
agenda = {}

    
def addNew(_input):
    _input = _input.split()
    nome = " ".join([n for n in _input if not 48 <= ord(n[0]) <= 57 ])
    telefones = [n for n in _input if 48 <= ord(n[0]) <= 57]
    print(nome,telefones)
    agenda[nome] = telefones
    print(agenda)

while choice != 0:
    system("cls||clear")

    print("1- Incluir novo nome")
    print("2- Incluir Telefone")
    print("3- Excluir telefone")
    print("4- Excluir nome")
    print("0- Sair")
    print()

    choice = int(input("> "))

    match choice:
        case 1:

           addNew(
                   input("Insira o nome a ser adicionado. Opcional: Insira numeros a serem adicionados ao nome, separados por espaço.\nExemplo: Cristiano Araujo 88994412 11223344\n> ")
                )

        case 2:
            
            nome = input("Insira o nome no qual os números serão adicionados: ")
            if nome not in agenda:
                if input("Esse nome não está na agenda, deseja adicioná-lo? (s/n): ") == "s":
                    addNew(nome +" "+input("digite os números a serem adicionados, separados por espaços: "))
            else:
                numeros = input("Digite os números a serem adicionados, separados por espaços: ")
                agenda[nome].extend(numeros.split())

        case 3:

            nome = input("Digite o nome a ser consultado: ")
            if nome in agenda:
                for index in range(len(agenda[nome])):
                    print(f"{str(index+1)} - {agenda[nome][index]}")
                print()
                index = int(input("Digite o número referente ao número a ser removido: "))
                if 0 <= index - 1 < len(agenda[nome]):
                    agenda[nome].pop(index - 1)
                    if len(agenda[nome]) == 0:
                        del agenda[nome]
                else:
                    print("Opção inválida!")
            else:
                print("Nome não encontrado na agenda")
                
        case 4:

            nome = input("Digite o nome a ser excluido: ")
            if nome in agenda:
                del agenda[nome]
            else:
                print("Nome inválido")
            
    input("\n\nPressione ENTER para continuar...")
