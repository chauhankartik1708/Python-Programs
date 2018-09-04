def palindrome(string):
    left = 0
    right = len(string)-1
    flag = False
    while(left<=right):
        if string[left] != string[right]:
            flag = False
            break
        else:
            flag = True
        left +=1
        right -=1

    if flag:
        print("Palindrome")
    else:
        print("Not Palindrome")
palindrome("nitin")
palindrome("kartik")