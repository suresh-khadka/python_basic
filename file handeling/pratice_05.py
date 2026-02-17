l=["donkey","dog","cat"]

with open("new.txt") as f:
    str= f.read()

for i in l:
    str=str.replace(i,"#"*len(i))
    print(i)

with open("new.txt","w") as f:
    f.write(str)
