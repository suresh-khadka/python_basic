f=open("student.txt","r")
str=f.readline()
while(str!=""):
    print(str)
    str=f.readline()
    print(type(str))

f.close()