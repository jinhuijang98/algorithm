import sys
input = sys.stdin.readline

T = int(input())

# 규칙 파악...
def plus_(n):
    if n == 1:
        return 1
    elif n == 2:
        return 2
    elif n == 3:
        return 4
    else:
        return plus_(n-1)+plus_(n-2)+plus_(n-3)

for tc in range(T):
    N = int(input())
    print(plus_(N))