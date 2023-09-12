import sys

input = sys.stdin.readline

T = int(input().strip())

for _ in range(T):
    n = int(input().strip())
    arr = list(map(int, input().strip().split()))
    i = n-1
    rlt = 0
    while i!=0:
        for j in range(i-1, -1, -1):
            if arr[i] > arr[j]:
                rlt += arr[i] - arr[j]
                arr[i], arr[j] = arr[j], arr[i]
                i = j
            else:
                i = j
                break
    print(rlt)

