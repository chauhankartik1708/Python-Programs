def transpose(A, B):
    for i in range(0,len(A)):
        for j in range(0,len(A)):
            B[j][i] = A[i][j]


A = [[1,1,1],
     [1,1,1],
     [1,1,1]]

B = [[0]*len(A[0]) for i in range(len(A))]
transpose(A, B)

print(A==B)