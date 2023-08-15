import sys
input = sys.stdin.readline
# 이차원 배열 시, 시간 초과
N = int(input())
stack = []
for _ in range(N):
    arr = list(map(int, input().split()))
    if len(arr) == 2:
        stack.append(arr[1])
    else:
        if arr == [2]:
            try:
                print(stack.pop())
            except:
                print(-1)
        elif arr == [3]:
            print(len(stack))
        elif arr == [4]:
            if len(stack)==0:
                print(1)
            else:
                print(0)
        else:
            if len(stack)==0:
                print(-1)
            else:
                print(stack[-1])
