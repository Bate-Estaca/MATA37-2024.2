vogais = ["a","e","i","o","u"]
vogaisQnt = 0

for letra in ["s","a","j","d","h","s","a","j","k","d","s","a","k","j","v","n","z","k","j","v","l","d","e","i","u","q"]:
    if letra.lower() in vogais:
        print(letra)
        vogaisQnt += 1
print("Vogais detectadas:",vogaisQnt)
