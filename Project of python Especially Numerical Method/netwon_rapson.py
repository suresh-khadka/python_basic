import math
def fx(x):
    return x*math.sin(x) + math.cos(x)

def dfx(x):
    return x*math.cos(x)

import random
x=random.randint(1,5)
e=0.0000001

def neteon_rapson(x):
    error=1
    while(error>e):
        x1=x-fx(x)/dfx(x)
        error=abs(x1-x)/x1
        x=x1
    return x

root=neteon_rapson(x)
print(f"root is : {root:.4f}")

import matplotlib.pyplot as plt
import numpy as np
x_vals = np.linspace(0, 5, 500)

y_vals = [fx(val) for val in x_vals]
plt.plot(x_vals, y_vals, label="f(x) = xsin(x) + cos(x)", color='blue')
plt.scatter(root ,0 , label=" root ", marker="*", color='red')
plt.title("Root of f(x)")
plt.xlabel("x")
plt.ylabel("f(x)")
plt.legend()
plt.grid(True)
plt.show()
