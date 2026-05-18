def input_X():
    x=[]
    n=int(input("enter number of values : "))
    for i in range(n):
        data=int(input("enter number of values : "))
        x.append(data)
    return x
# input from user
print(" enter value for X..........")
X=input_X()
print(X)
print(" enter value for Y..........")
Y=input_X()
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
result_x=sum_of_x(X)
result_y=sum_of_y(Y)
result_xsqu=sum_of_xsquare(X)
result_xy=sum_of_xy(X,Y)

c = (result_x*result_xsqu -  result_x* result_xy) / (n * result_xsqu - result_x**2)
m = (n * result_xy - result_x * result_y) / (n * result_xsqu - result_x**2)

print("\nLeast Squares Linear Fit:")
print(f"Equation: y = {m:.4f}x + {c:.4f}")

# Plotting (Optional)
import matplotlib.pyplot as plt

plt.scatter(X, Y, color='red', label='Data points')
y_fit = [m*x + c for x in X]
plt.plot(X, y_fit, color='blue', label='Best fit line')
plt.xlabel('X')
plt.ylabel('Y')
plt.title('Least Squares Fit Line')
plt.legend()
plt.grid(True)
plt.show()