fh = open("names.txt")

lst=[]
newlst=[]
for line in fh:
  line = line.strip()
  lst.append(line)

for word in lst:
    bracket=word.find("[")
    word = word[:bracket]
    newlst.append(word)

print(newlst)
#add a save to textfile
