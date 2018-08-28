rows = 5
row = 1
while (row <= rows):
    value = 1
    col = 0
    while(col<=row):
        print(value,end="\t")
        value = (value * (row - col)//(col + 1))
        col +=1
    print()
    row+=1
