def input_X():
    x=[]
    n=int(input("enter number of values : "))
    for i in range(n):
        data=int(input("enter number of values : "))
        x.append(data)
    return x

# lets take a sample
X=[2,4,6,8,10]
Y=[4.077,7.084,30.128,89.897,222.62]

import math
Y = [math.log(x) for x in Y]
print(Y)

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

def sum_of_xsquare(X):
    sum=0
    for i in range(len(X)):
        sum=sum+X[i]*X[i]
    return sum

def sum_of_xy(X,Y):
    sum=0
    for i in range(len(X)):
        sum=sum+X[i]*Y[i]
    return sum

n=len(X)
r_x=sum_of_x(X)
r_y=sum_of_y(Y)
r_xsqu=sum_of_xsquare(X)
r_xy=sum_of_xy(X,Y)

import numpy as np
print("augmented matrix become.......")
matrix=np.array([[n,r_x,r_y],[r_x,r_xsqu,r_xy]])
print(matrix)

def matrix_operation(mat):
    rows=len(mat)
    cols=len(mat[0])
   
    
    for j in range(cols):
        if(j==cols-1):
            break
        for i in range(rows):
            if i != j:
                value = mat[i][j] / mat[j][j]
                mat[i] = mat[i] - (value * mat[j])

    return mat

solve_matrix=matrix_operation(matrix)

def find_solution(mat):
    rows=len(mat)
    cols=len(mat[0])
    new_x=[]
    
    for j in range(cols):
        if(j==cols-1):
            break
        for i in range(rows):
            if(i==j):
                x=mat[i][cols-1]/mat[i][i]
                new_x.append(x)
    return new_x

result=find_solution(solve_matrix)
print(result)

def final_equation(res):
    print("\n<<<<<final equation become <<<<<<<<>>>>>>>>>>")
    print(f"y = {math.exp(res[0]):.3f} + {res[1]:.2f}x ")

final_equation(result)
import matplotlib.pyplot as plt
import numpy as np

# Original X values
X_vals = X

# Use result from your model: result[0] = a, result[1] = b
a = math.exp(result[0])
b = result[1]

# Generate smooth x values for curve
x_fit = np.linspace(min(X), max(X), 100)

# Compute predicted y = A * e^(bx)
y_fit = a * np.exp(b * x_fit)

# Plot original data points
plt.scatter(X, [math.exp(y) for y in Y], color='red', label='Original Data')

# Plot fitted curve
plt.plot(x_fit, y_fit, color='blue', label='Exponential Fit')

# Labels and title
plt.xlabel("X")
plt.ylabel("Y")
plt.title("Exponential Curve Fit")
plt.grid(True)
plt.legend()
plt.show()