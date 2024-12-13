word = input("Digite uma palavra: ")
chars = {}

for letter in word:
    if letter not in chars:
        chars[letter] = word.count(letter)

print(chars)
