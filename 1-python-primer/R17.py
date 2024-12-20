def r17(n):
    result = sum(a ** 2 for a in range(1, n) if a % 2 == 1 )
    print(result)