import numpy as np
import matplotlib.pyplot as plt

# Change the equation here:
def f(x, y):
    return x * y   # <--- This is the new differential equation

def rkf45(f, x0, y0, x_end, h_init=0.1, tol=1e-5):
    x_vals = [x0]
    y_vals = [y0]
    h = h_init
    x, y = x0, y0
    while x < x_end:
        if x + h > x_end:
            h = x_end - x
        k1 = h * f(x, y)
        k2 = h * f(x + 1/4*h, y + 1/4*k1)
        k3 = h * f(x + 3/8*h, y + 3/32*k1 + 9/32*k2)
        k4 = h * f(x + 12/13*h, y + 1932/2197*k1 - 7200/2197*k2 + 7296/2197*k3)
        k5 = h * f(x + h, y + 439/216*k1 - 8*k2 + 3680/513*k3 - 845/4104*k4)
        k6 = h * f(x + 1/2*h, y - 8/27*k1 + 2*k2 - 3544/2565*k3 + 1859/4104*k4 - 11/40*k5)
        y4 = y + 25/216*k1 + 1408/2565*k3 + 2197/4104*k4 - 1/5*k5
        y5 = y + 16/135*k1 + 6656/12825*k3 + 28561/56430*k4 - 9/50*k5 + 2/55*k6
        error = abs(y5 - y4)
        if error < tol:
            x += h
            y = y5
            x_vals.append(x)
            y_vals.append(y)
        if error == 0:
            s = 2
        else:
            s = 0.84 * (tol * h / error) ** 0.25
        h = min(h * s, 0.5)
    return np.array(x_vals), np.array(y_vals)

# Example usage
x0, y0 = 0, 1
x_end = 2
x_vals, y_vals = rkf45(f, x0, y0, x_end)

# Plotting the solution
plt.plot(x_vals, y_vals, label="RKF45 Solution")
plt.xlabel("x")
plt.ylabel("y")
plt.title("Solution of dy/dx = x * y using RKF45")
plt.grid(True)
plt.legend()
plt.show()
