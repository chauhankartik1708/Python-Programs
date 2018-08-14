my_list = [0,1,2,3,4,5,6,7,8,9]

for counter in range(0,len(my_list)):
    if counter in (0,4,5):
        del my_list[counter]


print(my_list)