word="donkey"

with open("new.txt") as f:
    str=f.read()

str_new=str.replace(word,"###")

with open("new.txt","w") as f:
    f.write(str_new)


