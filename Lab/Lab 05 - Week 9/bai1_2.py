import numpy as np

def split(matrix):
    row, col = matrix.shape
    row2, col2 = row//2, col//2
    return matrix[:row2, :col2], matrix[:row2, col2:], matrix[row2:, :col2], matrix[row2:, col2:]

def strassen(A, B):
    if (len(A)==1):
        return A*B
    # split matrix A to A1, A2, A3, A4
    A1, A2, A3, A4 = split(A)

    # split matrix B to B1, B2, B3, B4
    B1, B2, B3, B4 = split(B)

    # caculate M
    M1 = strassen((A1+A4), (B1+B4))
    M2 = strassen((A3+A4), B1)
    M3 = strassen(A1, (B2-B4))
    M4 = strassen(A4, (B3-B1))
    M5 = strassen((A1+A2), B4)
    M6 = strassen((A3-A1), (B1+B2))
    M7 = strassen((A2-A4), (B3+B4))

    C1 = M1+M4-M5+M7
    C2 = M3+M5
    C3 = M2+M4
    C4 = M1+M3-M2+M6

    # Combining the 4 quadrants into a single matrix by stacking horizontally and vertically.
    C = np.vstack((np.hstack((C1, C2)), np.hstack((C3, C4))))

    return C

n = int(input("Input n: "))

if((n%2)==0):
    A = np.random.randint(1, 1001, size=(n,n))
    B = np.random.randint(1, 1001, size=(n,n))
    print("- Matrix A is:\n",A)
    print("- Matrix B is:\n",B)
    C = strassen(A,B)
else:
    A = np.random.randint(1, 1001, size=(n,n))
    B = np.random.randint(1, 1001, size=(n,n))
    print("- Matrix A is:\n",A)
    print("- Matrix B is:\n",B)
    A_padded = np.pad(A, ((0, 1), (0, 1)), mode='constant')
    B_padded = np.pad(B, ((0, 1), (0, 1)), mode='constant')
    print("- Padded Matrix A is:\n",A_padded)
    print("- Padded Matrix B is:\n",B_padded)
    C = strassen(A_padded, B_padded)[:n, :n]
print("- Matrix C=A*B is:\n",C)