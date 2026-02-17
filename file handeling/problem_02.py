f=open("new.txt","w")
str=input("enter any string whixh you want to write on a file : ")
f.write(str)
f.close()

f=open("student.txt","r")
data=f.read()
print(data)
f.close()