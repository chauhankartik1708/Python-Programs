def checkEmpty(my_list):
    if len(my_list) == 0:
        print("List is empty")
    else:
        print("List is not empty")

my_list = [1,22,3,43]
other_list = []
checkEmpty(my_list)
checkEmpty(other_list)