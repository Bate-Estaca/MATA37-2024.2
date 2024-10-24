

num = int(input("Informe um número: "))
mul = 0

while mul<=10:
    resultado = num*mul
    if resultado % 2 != 0:
        print(num, "x", mul, "=", resultado)
    mul += 1
