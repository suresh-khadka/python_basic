
# input from user
def input_X():
    x=[]
    n=int(input("enter number of values : "))
    for i in range(n):
        data=int(input("enter number of values : "))
        x.append(data)
    return x

# lets take a sample
X=[1,2,3,4]
Y=[0.5,2,5,7.5]
# print(" enter value for X..........")
# X=input_X()
# print(X)
# print(" enter value for Y..........")
# Y=input_X()
# print(Y)

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


n=len(X)
r_x=sum_of_x(X)
r_y=sum_of_y(Y)
r_xsqu=sum_of_xsquare(X)
r_xy=sum_of_xy(X,Y)
r_x3=sum_of_x3(X)
r_x4=sum_of_x4(X)
r_x2y=sum_of_x2y(X,Y)

import numpy as np
print("augmented matrix become.......")
matrix=np.array([[n,r_x,r_xsqu,r_y],[r_x,r_xsqu,r_x3,r_xy],[r_xsqu,r_x3,r_x4,r_x2y]])
print(matrix)

def matrix_operation(mat):
    rows=len(mat)
    cols=len(mat[0])
   
    
    for j in range(cols):
        if(j==cols-1):
            break
        for i in range(rows):  # row operations: j is row index
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
                # print(f"x{i} = {x}")
    return new_x

result=find_solution(solve_matrix)
print(result)

def final_equation(res):
    print("\n<<<<<final equation become <<<<<<<<>>>>>>>>>>")
    print(f"y = {res[0]} + {res[1]}x +{ res[2]}x^2")

final_equation(result)

import matplotlib.pyplot as plt
import numpy as np

# Convert X and Y to numpy arrays for plotting
X = np.array(X)
Y = np.array(Y)

# Create a smooth range of x-values for plotting the fitted curve
x_fit = np.linspace(min(X), max(X), 100)

# Get coefficients from result
a, b, c = result  # result = [a, b, c]

# Calculate corresponding y-values for the fitted polynomial
y_fit = a + b * x_fit + c * x_fit**2

# Plot original data points
plt.scatter(X, Y, color='red', label='Original Data')

# Plot fitted curve
plt.plot(x_fit, y_fit, color='blue', label='Fitted Polynomial Curve')

# Add labels and title
plt.xlabel('X')
plt.ylabel('Y')
plt.title('2nd Degree Polynomial Fit')
plt.legend()
plt.grid(True)
plt.show()
