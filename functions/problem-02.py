def factorial(n):
    if(n==1):
        return 1
    elif(n==0):
        return 1
    else:
        return n*factorial(n-1)

n=int(input("enter any number : "))
a=factorial(n)
print(f"tne factorial of {n} is {a}")