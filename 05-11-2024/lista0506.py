n = int(input("Insira um número: "))

if (n == 1) | (n == 2):
    print(1)
else:
    before = 1
    actual = 1
    fibonacci = 0
    for value in range (3, n+1):
       fibonacci = before + actual
       before = actual
       actual = fibonacci

print(fibonacci)
