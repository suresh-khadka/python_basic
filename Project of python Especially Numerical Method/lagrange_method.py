import numpy as np
x=np.array([0,1,2,3,4])
y=np.array([-13,-16,-13,2,35])

def lagrange_method(x,y,X):
    sum=0
    for i in range(len(x)):
        mul=1
        for j in range(len(x)):
            if(i!=j):
                mul=mul*(X-x[j])/(x[i]-x[j])
            else:
                continue

        sum=sum+mul*y[i]

    return sum

result=lagrange_method(x,y,3.3)
print(result)

x_smooth = np.linspace(min(x), max(x), 200)
y_smooth = [lagrange_method(x, y, i) for i in x_smooth]


import matplotlib.pyplot as plt
plt.plot(x_smooth,y_smooth,label=" lagrange method ",color="blue")
plt.scatter(3.3,result,color="red")
plt.title("lagrange method")
plt.xlabel("x")
plt.ylabel("y")
plt.legend()
plt.grid(True)
plt.show()

