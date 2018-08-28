import math
A = [[1,2,3],
     [4,5,6],
     [7,8,9]]

sum = 0

for i in range(len(A)):
    for j in range(len(A[0])):
        sum += (A[i][j] * A[i][j])

print(sum)
print(math.sqrt(sum))