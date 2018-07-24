def prime(n):
    i = 2
    while i < n:
        if n % i == 0:
            print(str(n) + " is not prime")
            return
        i = i + 1
    print(str(n) + " is prime")

def fibo(n):
    a = 0
    b = 1
    i = 2
    sum = 0

    if n == 0:
        print(a)
    elif n == 1:
        print(b)
    else:
        while i <= n:
            sum = a+b
            a = b
            b = sum
            i = i+1
        print(str(n) + "th Fibonacci is " + str(sum))

def factorial(n):
    if n==0:
        return 1
    return n * factorial(n-1)

print(prime(31))
print(fibo(3))
print(factorial(5))