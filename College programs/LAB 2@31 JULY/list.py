inputs = int(input("Enter no. of inputs : "))
mylist=[]
for i in range(0,inputs):
    mylist.append(str(input()))

print(mylist)

mytuple = tuple(mylist)
print(mytuple)

dicinput = int(input("Enter no. of inputs : "))
mydic={}
for i in range(0,dicinput):
    text = input().split()
    mydic[text[0]] = text[1]

print(mydic)