import math
import random
def fx(x):
    return x*math.sin(x) + math.cos(x)

a=random.randint(1,5)
b=random.randint(1,5)
print(a,b)

# e=float(input("enter value of telerance : "))
e=0.00000000001

def secent_method(a,b,e):
    c=0
    while(abs(fx(c))>e):
        c=(a*fx(b)-b*fx(a))/(fx(b)-fx(a))
        a=b
        b=c
    return c

root=secent_method(a,b,e)
print(f"root is : {root:.4f}")
            