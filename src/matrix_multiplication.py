def classical_multiply(A, B):
    n = len(A)
    # initialize an n x n matrix with zeros
    C = [[0 for _ in range(n)] for _ in range(n)]

    # 3 nested loops for O(n^3) complexity
    for i in range(n):
        for j in range(n):
            for k in range(n):
                C[i][j] += A[i][k] * B[k][j]
    return C


def add_matrices(A, B):
    return [[A[i][j] + B[i][j] for j in range(len(A[0]))] for i in range(len(A))]


def sub_matrices(A, B):
    return [[A[i][j] - B[i][j] for j in range(len(A[0]))] for i in range(len(A))]


def strassen_multiply(A, B):
    n = len(A)

    # 1x1 matrix
    if n == 1:
        return [[A[0][0] * B[0][0]]]

    mid = n // 2

    # slice the matrices into quadrants
    a11 = [row[:mid] for row in A[:mid]]
    a12 = [row[mid:] for row in A[:mid]]
    a21 = [row[:mid] for row in A[mid:]]
    a22 = [row[mid:] for row in A[mid:]]

    b11 = [row[:mid] for row in B[:mid]]
    b12 = [row[mid:] for row in B[:mid]]
    b21 = [row[:mid] for row in B[mid:]]
    b22 = [row[mid:] for row in B[mid:]]

    # 7 Strassen multiplications
    p1 = strassen_multiply(a11, sub_matrices(b12, b22))
    p2 = strassen_multiply(add_matrices(a11, a12), b22)
    p3 = strassen_multiply(add_matrices(a21, a22), b11)
    p4 = strassen_multiply(a22, sub_matrices(b21, b11))
    p5 = strassen_multiply(add_matrices(a11, a22), add_matrices(b11, b22))
    p6 = strassen_multiply(sub_matrices(a12, a22), add_matrices(b21, b22))
    p7 = strassen_multiply(sub_matrices(a11, a21), add_matrices(b11, b12))

    # combining the 7 products into 4 quadrants
    c11 = add_matrices(sub_matrices(add_matrices(p5, p4), p2), p6)
    c12 = add_matrices(p1, p2)
    c21 = add_matrices(p3, p4)
    c22 = sub_matrices(sub_matrices(add_matrices(p5, p1), p3), p7)

    # reconstructing final matrix C
    C = []
    for i in range(mid):
        C.append(c11[i] + c12[i])
    for i in range(mid):
        C.append(c21[i] + c22[i])

    return C