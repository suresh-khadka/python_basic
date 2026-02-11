name=[]
lan=[]
dic={}
for i in range(4):
    n=input("eneter name ")
    l=input("enetr language")
    # name.append(n)
    # lan.append(l)
    dic.update({n:l})   #same as below
    # dic[n]=l         #same result as above
print(dic)