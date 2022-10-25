# write a code for gauss elimination

# A = [[0, 5, -12], [-9, 0, 4], [7, 0, 3]]
# b = [3, 3, 6]
A = [[0,7,-1,3,1],[0,3,4,1,7],[6,2,0,2,-1],[2,1,2,0,2],[3,4,1,-2,1]]
b = [5,7,2,3,4]


for k in range(len(A)):
    # pivoting
    if A[k][k] == 0:
        # swap rows to make the pivot non-zero
        imax = max(range(k, len(A)), key=lambda i: abs(A[i][k]))
        A[k], A[imax] = A[imax], A[k]
    for i in range(k + 1, len(A)):
        m = A[i][k] / A[k][k]
        b[i] = b[i] - m * b[k]
        for j in range(k, len(A[0])):
            A[i][j] = A[i][j] - m * A[k][j]

# back substitution
print(A)
for k in range(len(A) - 1, -1, -1):
    b[k] = b[k] / A[k][k]
    for i in range(k - 1, -1, -1):
        b[i] = b[i] - A[i][k] * b[k]

print(b)
