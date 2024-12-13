wordlist = open("./words.txt","r").read().split("\n")
words = {}

for n in range(len( wordlist)):
    words[wordlist[n]]=n

print(words)
