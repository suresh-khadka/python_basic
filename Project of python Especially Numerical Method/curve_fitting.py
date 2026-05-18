# exponential finction : y=a.e^x
import numpy as np 
x=np.array([2,4,6,8,10])
y=np.array([4.077,11.084,30.128,81.897,222.62])

import math
n=len(x)
sum_x=np.sum(x)
sum_y=np.sum(math.log(i) for i in y)
sum_xy=np.sum(x*math.log(i) for x,i in zip(x,y))
sum_xsqu=np.sum(x**2)

def exponential_fitting(n,sx,sy,sxy,sx2):
    det=np.linalg.det([[n,sx],[sx,sx2]])
    det_a=np.linalg.det([[sy,sx],[sxy,sx2]])
    det_b=np.linalg.det([[n,sy],[sx,sxy]])
    a=det_a/det
    b=det_b/det
    return a,b


a,b=exponential_fitting(n,sum_x,sum_y,sum_xy,sum_xsqu)
A=math.exp(a)
print(f" value of A = {A:.4f} \n vlue of  b = {b:.4f}")

import matplotlib.pyplot as plt
x_val=np.linspace(min(x)-1,max(x)+1,399)
y_val=[A*math.exp(b*x) for x in x_val]
plt.plot(x_val,y_val,label="exponential fitting", color="blue")
plt.scatter(x,y,color="red")
plt.title("exponential fitting")
plt.xlabel("x")
plt.ylabel("y")
plt.legend()
plt.grid(True)
plt.show()