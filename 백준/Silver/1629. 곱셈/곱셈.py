def reduce_pow(a, b, c):
    if (b == 1):
        return a % c

    X = reduce_pow(a, b//2, c)

    if (b % 2 == 0): 
        return X * X % c
    else: 
        return a * X * X % c

A, B, C = map(int, input().split())

print(reduce_pow(A, B, C))