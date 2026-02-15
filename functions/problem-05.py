def sum(n):
    if(n==0):
        return 0
    else:
        return n+sum(n-1)
    
a=int(input("enter any number : "))
b=sum(a)
print("sum of ",a ,"is",b)