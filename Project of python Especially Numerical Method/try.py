

def enter_column(n):
    column = []
    for i in range(n):
        a = int(input(f"Enter element {i+1}: "))
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
matrixx=np.array(matrix1,dtype=float)
print(type(matrixx))
print(matrixx)


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

solve_matrix=matrix_operation(matrixx)
print(solve_matrix)

def find_solution(mat):
    rows=len(mat)
    cols=len(mat[0])
   
    
    for j in range(cols):
        if(j==cols-1):
            break
        for i in range(rows):
            if(i==j):
                print(mat[i][cols-1])
                x=mat[i][cols-1]/mat[i][i]
                print(f"x{i} = {x}")


find_solution(solve_matrix)