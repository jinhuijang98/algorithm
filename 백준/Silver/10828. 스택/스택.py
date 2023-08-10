import sys
input = sys.stdin.readline

N = int(input())
arr = []
for i in range(N):
    text = input().strip('\n')
    if "push" in text:
        arr.append(text.split(' ')[1])
    elif "top" in text:
        try:
            print(arr[-1])
        except:
            print(-1)

    elif "size" in text:
        print(len(arr))
    elif "empty" in text:
        if len(arr) == 0:
            print(1)
        else:
            print(0)
    else:
        try:
            print(arr.pop())
        except:
            print(-1)