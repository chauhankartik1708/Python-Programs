def transpose(A, B):
    for i in range(len(A[0])):
        for j in range(len(A)):
            B[j][i] = A[i][j]


# driver code
A = [[1,2,3],
     [4,5,6],
     [7,8,9]]

B = A[:][:]  # To store result

transpose(A, B)

print("Result matrix is")
for i in B:
    print(i)