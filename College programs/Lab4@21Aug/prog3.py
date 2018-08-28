def add(X,Y,result):
    for i in range(0,len(X)):
        for j in range(0,len(X[0])):
            result[i][j] = X[i][j] + Y[i][j]

def subtract(X,Y,result):
    for i in range(0,len(X)):
        for j in range(0,len(X[0])):
            result[i][j] = X[i][j] - Y[i][j]



X = [[1, 2, 3],
     [4, 5, 6],
     [7, 8, 9]]

Y = [[9, 8, 7],
     [6, 5, 4],
     [3, 2, 1]]

added = [[0]*len(X[0]) for i in range(len(X))]
subtracted = [[0]*len(X[0]) for i in range(len(X))]
add(X,Y,added)
subtract(X,Y,subtracted)

for r in added:
    print(r)
for r in subtracted:
    print(r)