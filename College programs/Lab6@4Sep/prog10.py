import random
def rand():
    randomNum = random.randint(0,100)
    print(randomNum)
    return (randomNum + ord(chr(randomNum)))

print(rand())