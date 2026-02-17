import numpy as np

np.random.seed(0)
x = np.linspace(0, 10, 1000)
y = 3 * x + 5 + np.random.normal(0, 5, size=1000) 
print(f"value of x : {x}")
print(f"value of y : {y}")
