def reverse(list):
    left = 0
    right = len(list) -1
    while(left<=right):
        temp = list[left]
        list[left] = list[right]
        list[right] = temp
        left +=1
        right -=1
    return list

def recursiveReverse(list,vidx):
    if(vidx == len(list)):
        return

    recursiveReverse(list,vidx+1)
    print(str(list[vidx]) + ", ",end="")


list = [1,2,3,4,5]
list2 = [1,2,3,4,5]
print(list)
print(reverse(list))
print("Recursive : ")
print("[",end="")
recursiveReverse(list2,0)
print("]")