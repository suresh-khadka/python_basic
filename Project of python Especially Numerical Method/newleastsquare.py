def input_X():
    x = []
    n = int(input("enter number of values : "))
    for i in range(n):
        data = int(input("enter number of values : "))
        x.append(data)
    return x

# input from user
print(" enter value for X..........")
X = input_X()
print(X)
print(" enter value for Y..........")
Y = input_X()   # fixed: added () to call the function
print(Y)

def sum_of_x(X):
    sum = 0
    for i in range(len(X)):
        sum = sum + X[i]
    return sum

def sum_of_y(Y):
    sum = 0
    for i in range(len(Y)):
        sum = sum + Y[i]
    return sum

def sum_of_xsquare(X):
    sum = 0
    for i in range(len(X)):
        sum = sum + X[i] * X[i]
    return sum

def sum_of_xy(X, Y):   # fixed: added Y as parameter
    sum = 0
    for i in range(len(X)):
        sum = sum + X[i] * Y[i]
    return sum

n = len(X)
sum_x = sum_of_x(X)             # fixed: was sum__x()
sum_y = sum_of_y(Y)
sum_xsqu = sum_of_xsquare(X)
sum_xy = sum_of_xy(X, Y)        # fixed: added arguments

m = (n * sum_xy - sum_x * sum_y) / (n * sum_xsqu - sum_x ** 2)
c = (sum_y - m * sum_x) / n

print("\nLeast Squares Linear Fit:")
print(f"Equation: y = {m:.4f}x + {c:.4f}")

# Plotting (Optional)
import matplotlib.pyplot as plt

plt.scatter(X, Y, color='red', label='Data points')
y_fit = [m * x + c for x in X]
plt.plot(X, y_fit, color='blue', label='Best fit line')
plt.xlabel('X')
plt.ylabel('Y')
plt.title('Least Squares Fit Line')
plt.legend()
plt.grid(True)
plt.show()
