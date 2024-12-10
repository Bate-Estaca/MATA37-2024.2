
d = {"nome":"","idade":"","telefone":"","endereco":""}


for key in d.keys():
    d[key] = input(f"insira o valor de {key}: ")

temp = list(d)
temp.sort()

for key in temp :
    print(f"{key}: {d[key]}")
