a, b = map(str, input().split())

def rev(x):
    rev_x=''
    for i in range(len(x)-1, -1, -1):
        rev_x += x[i]
    return int(rev_x)

print(rev(str(rev(a) + rev(b))))