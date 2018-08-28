import sys
A = [[1,2,3],
     [4,5,6],
     [7,8,9]]
min = sys.maxsize
max = -sys.maxsize-1
print(max)
print(min)

for i in range(len(A)):
    for j in range(len(A[0])):
        if(A[i][j] >= max):
            max = A[i][j]
        if(A[i][j] <= min):
            min = A[i][j]

print(max)
print(min)