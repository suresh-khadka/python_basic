def remove(l,word):
    n=[]
    for item in l:
        if not(item==word):
            n.append(item.strip(word))
    
    return n

print("to add to list press 2")

l=[]
i=3
while(i!=1):
    a=input("add to list : ")
    l.append(a)
    i=int(input("you want to exit press ->1 ...if not press ->2: "))

print(l)
print("enter a word which want to remove : ")
s=input()
print(remove(l,s))