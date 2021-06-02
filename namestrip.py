fh = open("innerrim.txt")

lst = []

for line in fh:
    line = line.strip()
    lst.append(line)

for word in lst:
    bracket = word.find("[")
    word = word[:bracket]
    print(word)


