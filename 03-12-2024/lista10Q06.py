output = ""

for letter in input():
    lower = letter.lower()
    if not lower in ["a","e","i","o","u"]:
          output += lower

print(output)

