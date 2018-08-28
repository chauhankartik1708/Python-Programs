def transpose(A, B):
    for i in range(0,len(A)):
        for j in range(0,len(A)):
            B[j][i] = A[i][j]


A = [[1,2,3],
     [4,5,6],
     [7,8,9]]

B = [[0]*len(A[0]) for i in range(len(A))]
transpose(A, B)

print("Result matrix is")
for i in B:
    print(i)