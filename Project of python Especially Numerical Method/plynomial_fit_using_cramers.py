def sum_of_x(X):
    sum=0
    for i in range(len(X)):
        sum=sum+X[i]
    return sum

def sum_of_y(Y):
    sum = 0
    for i in range(len(Y)):
        sum = sum + Y[i]
    return sum

def sum_of_x2(X):
    sum=0
    for i in range(len(X)):
        sum=sum+X[i]*X[i]
    return sum

def sum_of_xy(X,Y):
    sum=0
    for i in range(len(X)):
        sum=sum+X[i]*Y[i]
    return sum
def sum_of_x3(X):
    sum=0
    for i in range(len(X)):
        sum=sum+X[i]*X[i]*X[i]
    return sum
def sum_of_x4(X):
    sum=0
    for i in range(len(X)):
        sum=sum+X[i]*X[i]*X[i]*X[i]
    return sum
def sum_of_x2y(X,Y):
    sum=0
    for i in range(len(X)):
        sum=sum+X[i]*X[i]*Y[i]
    return sum
def sum_of_x5(X):
    sum=0
    for i in range(len(X)):
        sum=sum+X[i]*X[i]*X[i]*X[i]*X[i]
    return sum
def sum_of_x3y(X,Y):
    sum=0
    for i in range(len(X)):
        sum=sum+X[i]*X[i]*Y[i]*X[i]
    return sum
def sum_of_x6(X):
    sum=0
    for i in range(len(X)):
        sum=sum+X[i]*X[i]*X[i]*X[i]*X[i]*X[i]
    return sum
def sum_of_x4y(X,Y):
    sum=0
    for i in range(len(X)):
        sum=sum+X[i]*X[i]*Y[i]*X[i]*X[i]
    return sum

def sum_of_x7(X):
    sum=0
    for i in range(len(X)):
        sum=sum+X[i]*X[i]*X[i]*X[i]*X[i]*X[i]*X[i]
    return sum
def sum_of_x8(X):
    sum=0
    for i in range(len(X)):
        sum=sum+X[i]*X[i]*X[i]*X[i]*X[i]*X[i]*X[i]*X[i]
    return sum


# lets take a sample
X = [-4, -3, -2, -1.5, -1, -0.5, 0, 0.5, 1, 1.5, 2, 2.5, 3, 4]
Y = [400, 150, 38, 20, 8, 5, 2, 4, 9, 20, 50, 95, 200, 310]


n=len(X)
r_x=sum_of_x(X)
r_y=sum_of_y(Y)
r_x2=sum_of_x2(X)
r_x3=sum_of_x3(X)
r_x4=sum_of_x4(X)
r_X5=sum_of_x5(X)
r_x6=sum_of_x6(X)
r_x7=sum_of_x7(X)
r_x8=sum_of_x8(X)
r_xy=sum_of_xy(X,Y)
r_x2y=sum_of_x2y(X,Y)
r_x3y=sum_of_x3y(X,Y)
r_x4y=sum_of_x4y(X,Y)

import numpy as np
import matplotlib.pyplot as plt
delta=np.linalg.det([[n,r_x,r_x2,r_x3,r_x4],[r_x,r_x2,r_x3,r_x4,r_X5],[r_x2,r_x3,r_x4,r_X5,r_x6],[r_x3,r_x4,r_X5,r_x6,r_x7],[r_x4,r_X5,r_x6,r_x7,r_x8]])
delta1=np.linalg.det([[r_y,r_x,r_x2,r_x3,r_x4],[r_xy,r_x2,r_x3,r_x4,r_X5],[r_x2y,r_x3,r_x4,r_X5,r_x6],[r_x3y,r_x4,r_X5,r_x6,r_x7],[r_x4y,r_X5,r_x6,r_x7,r_x8]])
delta2=np.linalg.det([[n,r_y,r_x2,r_x3,r_x4],[r_x,r_xy,r_x3,r_x4,r_X5],[r_x2,r_x2y,r_x4,r_X5,r_x6],[r_x3,r_x3y,r_X5,r_x6,r_x7],[r_x4,r_x4y,r_x6,r_x7,r_x8]])
delta3=np.linalg.det([[n,r_x,r_y,r_x3,r_x4],[r_x,r_x2,r_xy,r_x4,r_X5],[r_x2,r_x3,r_x2y,r_X5,r_x6],[r_x3,r_x4,r_x3y,r_x6,r_x7],[r_x4,r_X5,r_x4y,r_x7,r_x8]])
delta4=np.linalg.det([[n,r_x,r_x2,r_y,r_x4],[r_x,r_x2,r_x3,r_xy,r_X5],[r_x2,r_x3,r_x4,r_x2y,r_x6],[r_x3,r_x4,r_X5,r_x3y,r_x7],[r_x4,r_X5,r_x6,r_x4y,r_x8]])
delta5=np.linalg.det([[n,r_x,r_x2,r_x3,r_y],[r_x,r_x2,r_x3,r_x4,r_xy],[r_x2,r_x3,r_x4,r_X5,r_x2y],[r_x3,r_x4,r_X5,r_x6,r_x3y],[r_x4,r_X5,r_x6,r_x7,r_x4y]])

a=delta1/delta
b=delta2/delta
c=delta3/delta
d=delta4/delta
e=delta5/delta

print("The fourth order polynomimal is : ")
print(f"Y = {a} + {b}X + {c}X^2 + {d}X^4")

# Visualization
x_vals = np.linspace(min(X), max(X), 200)  # Smooth x range
y_vals = a + b*x_vals + c*x_vals**2 + d*x_vals**3 + e*x_vals**4  # 4th-degree polynomial

# Original data points
plt.scatter(X, Y, color='red', label='Original Data')

# Polynomial curve
plt.plot(x_vals, y_vals, color='blue', label='4th-degree Polynomial Fit')

# Labels and title
plt.xlabel("X")
plt.ylabel("Y")
plt.title("4th-Degree Polynomial Fit")
plt.grid(True)
plt.legend()
plt.show()
