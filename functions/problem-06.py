def design(n):
    if(n==0):
        return 1
    
    print(n*"*")
    design(n-1)


print("if you want to print n number of *")
a=int(input("enter nuber of star : "))
design(a)