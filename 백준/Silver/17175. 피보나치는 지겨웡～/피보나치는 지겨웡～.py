n = int(input())

if n < 2:
    print(1)
else:
    a, b = 1, 1
    for i in range(n-1):
        a, b = a+b+1, a
    print(a%1000000007)