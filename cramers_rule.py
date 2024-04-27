import numpy as np
fname1 = input("Enter file of the matrix: ")
fname2 = input("Enter file of the vector: ")

if len(fname1) < 1 : fname1 = "matrix_cramer1.txt"
if len(fname2) < 1 : fname2 = "vector1.txt"
#Makes Matrix and Vector
i1 = np.loadtxt(fname1, dtype='i', delimiter=',')
i2 = np.loadtxt(fname2, dtype='i', delimiter=',')
print("Matrix is : ")
print(i1)
print("Vector is : ")
print(i2)
def cramer(mat, constant):
    # Calculate the determinant of the original matrix
    D = np.linalg.det(mat)

    # Create matrices by substituting each column with the constant vector
    mat1 = np.array([constant, mat[:, 1], mat[:, 2]])
    mat2 = np.array([mat[:, 0], constant, mat[:, 2]])
    mat3 = np.array([mat[:, 0], mat[:, 1], constant])

    # Calculate the determinants of the modified matrices
    D1 = np.linalg.det(mat1)
    D2 = np.linalg.det(mat2)
    D3 = np.linalg.det(mat3)

    # Find the solution vector (X1, X2, X3)
    X1 = D1 / D
    X2 = D2 / D
    X3 = D3 / D

    return X1, X2, X3

# calculating the determinant of matrix 
det = np.linalg.det(i1) 
print("\nDeterminant of given 3X3 matrix:") 
print(int(det))
X1, X2, X3 = cramer(i1, i2)
print(f"Solution of Cramer's rule : X1 = {X1}, X2 = {X2}, X3 = {X3}")