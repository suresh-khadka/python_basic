import math
def fx(x):
    return x*math.sin(x) + math.cos(x)

def find_value_of_a():
    for i in range(1,5):
        if((fx(i)<0 and fx(i+1)>0) or (fx(i)<0 and fx(i-1)>0) ):
            return i
    
def find_value_of_b():
    for i in range(1,5):
        if((fx(i)>0 and fx(i+1)<0) or (fx(i)>0 and fx(i-1)<0) ):
            return i


a=find_value_of_a()
b=find_value_of_b()
print(a,b)

e=float(input("enter value of telerance : "))

def bisection_method(a,b,e):
    c=0
    while(abs(fx(c))>e):
        c=(a+b)/2
        if(fx(c)<0):
            a=c
        else:
            b=c
    return c

root=bisection_method(a,b,e)
print(f"root is : {root:.4f}")
            