def enter_column(n):
    column = []
    for i in range(n):
        a = float(input(f"Enter element {i+1}: "))
        column.append(a)
    return column

def matrix(rows, cols):
    mat = []
    for i in range(rows):
        print(f"\nEnter row {i+1}:")
        new_row = enter_column(cols)
        mat.append(new_row)
    return mat

# Input
print("Enter augmented matrix:")
ro = int(input("Enter number of rows: "))
co = int(input("Enter number of columns: "))

matrix1 = matrix(ro, co)

import numpy as np
matrixx = np.array(matrix1, dtype=float)
print("\nInitial Augmented Matrix:")
print(matrixx)


def matrix_operation(mat):
    rows = len(mat)
    cols = len(mat[0])

    for i in range(rows):
        # Make diagonal element 1
        diag = mat[i][i]
        if diag == 0:
            continue  # skip if diagonal is zero (basic handling)
        mat[i] = mat[i] / diag

        for j in range(i + 1, rows):
            factor = mat[j][i]
            mat[j] = mat[j] - factor * mat[i]

    return mat

solve_matrix = matrix_operation(matrixx.copy())
print("\nMatrix after forward elimination:")
print(solve_matrix)


def find_solution(mat):
    rows = len(mat)
    cols = len(mat[0])
    x = [0 for _ in range(rows)]

    # Back substitution
    for i in range(rows - 1, -1, -1):
        x[i] = mat[i][cols - 1]
        for j in range(i + 1, rows):
            x[i] -= mat[i][j] * x[j]
    
    print("\nSolution:")
    for i in range(len(x)):
        print(f"x{i+1} = {x[i]:.4f}")

find_solution(solve_matrix)
