def fibonacci (n) :
    if n < 2:
        return n
    else :
        return fibonacci(n-1) + fibonacci(n-2)
    

n = int(input())

print ("값 : ", fibonacci(n))
    