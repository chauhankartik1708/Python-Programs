X = [[1, 2, 33],
     [4, 5, 63],
     [7, 83, 9]]

count = 0
for i in range(len(X)):
    for j in range(len(X[0])):
        if(((X[i][j])%10)== 3):
            count += 1
print(count)