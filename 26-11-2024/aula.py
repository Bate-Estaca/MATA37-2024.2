_str = "Aoba"

print(_str.upper())
print(_str.lower())

print("a" < "b")
print("a" < "B")

print(ord("A"))
print(chr(65))

print(_str[1:4])

_str = "Logica de Programacao"

print(_str[2::3])

#for char in _str:
#    print(char)
#

print("L" in _str)
print(_str.find("L"))
print(_str.count("o"))

print(list(_str))
Hello = ["H","e","l","l","o"]
print("".join(Hello))

print(_str.replace("o","O"))

#_str = "Meu nome é %s, tenho %d anos e tenho %.2f de altura" % ("Lucas",23,1.7132)
#_str = "Meu nome é {}, tenho {} anos e tenho {:.2f} de altura".format("Lucas",23,1.7132)
_str = f"Meu nome é {"Lucas"}, tenho {23} anos e tenho {1.7132:.2f} de altura"
print(_str)

print(dir(_str))
print(help(_str.find))
print(help(_str))
