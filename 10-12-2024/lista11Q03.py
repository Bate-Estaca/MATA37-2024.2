d = {"nome":"","idade":"","telefone":"","endereco":""}


for key in d.keys():
    d[key] = input(f"insira o valor de {key}: ")

print(d)
