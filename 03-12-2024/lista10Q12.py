from os import system 
from time import sleep

S1 = input("Digite uma string (max 20 chars): ")
if len(S1) > 20:
    print(f"\nA string {S1} possui {len(S1)} caracteres! O tamanho máximo permitido é 20!\n")
    sleep(3)
    exit(1)

def drawMenu():
    system("cls||clear")
    print("1- Tamanho da string")
    print("2- Comparar com outra string")
    print("3- Concatenar com outra string")
    print("4- Imprimir string ao reverso")
    print("5- Contar um caracter")
    print("6- Verificar subString")
    print("7- Criar subString")
drawMenu()

