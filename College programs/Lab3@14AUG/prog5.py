def common(list_A,list_B):
    common = []
    for i in list_A:
        if i in list_B:
            common.append(i)
    print(common)

list_A = [1,2,3,4]
list_B = [2,5,6,3]
common(list_A,list_B)
print(set(list_A) & set(list_B))
