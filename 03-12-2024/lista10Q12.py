from os import system 
from time import sleep

S1 = input("Digite uma string (max 20 chars): ")
if len(S1) > 20:
    print(f"\nA string {S1} possui {len(S1)} caracteres! O tamanho máximo permitido é 20!\n")
    sleep(3)
    exit(1)
    
def main():
   _exit = False
   system("cls||clear")
   while(not _exit):
        drawMenu()
        print("\n")
        _exit = choice(input("> "))
        input("Pressione ENTER para continuar...")
        system("cls||clear")

   return 0

def drawMenu():
   print("1- Tamanho da string")
   print("2- Comparar com outra string")
   print("3- Concatenar com outra string")
   print("4- Imprimir string ao reverso")
   print("5- Contar um caracter")
   print("6- Verificar subString")
   print("7- Criar subString")
   print()
   print("8. sair")
   print('\n\n')

def choice(expr):
    match int(expr):
        case 1:
            print(f"O tamanho da string \"{S1}\" é: {len(S1)}")
        case 2:
            print(input("Digite a string a ser comparada: ") == S1)
        case 3:
            print(S1 + input("Digite a string a ser concatenada: "))
        case 4:
            print("".join(list(S1)[::-1]))
        case 5:
            _char = input("Digite o caracter a ser contado: ")
            print(f"{_char}: ",S1.count(_char))
        case 6:
            print(S1.find(input("Digite a substring a ser procurada: ")) != -1)
        case 7:
            [start, lenght] = map(int, input("Insira o inicio e o tamanho da substring no format: INICIO TAMANHO").split())
            print(S1[start:start+lenght])
        case 8:
            return True
    return False

main()
