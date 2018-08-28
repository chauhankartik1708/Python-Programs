trace = 0

A = [[1,2,3],
     [4,5,6],
     [7,8,9]]

for i in range(len(A)):
    trace += A[i][i]

print(trace)