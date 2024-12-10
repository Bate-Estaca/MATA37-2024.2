phrase = input("Insira a frase: ")
offset = int(input("Insira o deslocamento: "))
output = ""

for letter in phrase:
    charCode = ord(letter)

    if offset > 25:
        offset = offset % 25
    if offset < -25:
        offset =  (offset % 25) - 25

    newCharCode = charCode + offset

    if letter.islower():

        if newCharCode < 97:
           newCharCode = charCode + 26 + offset
        if  newCharCode > 122:
            newCharCode = charCode - 26 + offset

    elif letter.isupper():

        if newCharCode < 65:
            newCharCode = charCode + 26 + offset
        if  newCharCode > 90:
            newCharCode = charCode - 26 + offset
    else:
        newCharCode = charCode
    output += chr(newCharCode)

print(output)
