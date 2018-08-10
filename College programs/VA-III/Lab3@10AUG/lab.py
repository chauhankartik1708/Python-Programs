def Remove(duplicate):
    final_list = []
    for num in duplicate:
        if num not in final_list:
            final_list.append(num)
    return final_list



duplicate = [2, 4, 10, 20, 5, 2, 20, 4]
print(Remove(duplicate))
#########

l1 = [1,2,3,4,5]
l2 = [6,7,8,9]
l1 = l1 + l2
print(l1)
###########
dicinput = int(input("Enter no. of inputs : "))
mydic={}
for i in range(0,dicinput):
    text = input().split()
    mydic[text[0]] = text[1]

print(mydic)
##########
abc = "kartik"
count = 0
itr = 0
list = ['a','o','i','e','u']
for character in abc:
    if abc[itr] in list:
        count = count + 1
    itr = itr + 1
print(count)

