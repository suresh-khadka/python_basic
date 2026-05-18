# def function():
#     a_in = []
#     a = int(input("Enter the number of unknown variables: "))
#     for i in range(a):
#         data = int(input(f"Enter the coefficient for x{i+1}: ")) 
#         a_in.append(data)
#     rhs = int(input("Enter the target value (RHS of the equation): "))
#     return a_in, rhs

# def display_eqn(ain, rhs):
#     for i in range(len(ain)):
#         print(f"{ain[i]}x{i+1}", end="") 
#         if i != len(ain) - 1:
#             print(" + ", end="")
#     print(f" = {rhs}")  # Print the RHS

# # Run the functions
# coeffs, target = function()
# display_eqn(coeffs, target)

# coeffs2, target2 = function()
# display_eqn(coeffs2, target2)

# coeffs3, target3 = function()
# display_eqn(coeffs3, target3)


coeffs = [2, 4, 8]
target = 15

coeffs2 = [1, 3, 5]
target2= 9

coeffs3 = [1, 4, 8]
target3 = 16

import numpy as np
A=np.array([coeffs,coeffs2,coeffs3])
B=np.array([target,target2,target3])
x = np.linalg.solve(A, B)
print(f"solve using python library : {x}")

def solve_eqn(coff1, target1, coff2, target2, coff3, target3):
    x0, y0, z0 = 0.0, 0.0, 0.0
    
    max_iteration = 0
    while max_iteration < 100:
        # Use the most updated values (Gauss-Seidel)
        x0 = (target1 - coff1[1]*y0 - coff1[2]*z0) / coff1[0]
        y0 = (target2 - coff2[0]*x0 - coff2[2]*z0) / coff2[1]
        z0 = (target3 - coff3[0]*x0 - coff3[1]*y0) / coff3[2]
        
        max_iteration += 1

    return x0, y0, z0


x, y, z = solve_eqn(coeffs, target, coeffs2, target2, coeffs3, target3)
print(f"x  = {x}, y = {y}, z = {z}")