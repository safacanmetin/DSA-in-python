def sqrsTillN(n):
    sum = 0
    for i in range(1,n):
        sum += i ** 2
        
    return sum