'''
8

10 7 8 9 10 2 4 13

답 >> 612

'''


import sys

input = sys.stdin.readline

n = int(input().strip())

arr = list(map(int, input().strip().split()))
rlt = 0
path = [0] * (n-2)
def backtracking(cnt):
    global rlt
    max_v = 0
    # 가지치기 => 조건?
    # 만약 path의 곱의 합이 rlt보다 작다면 return?
    if cnt == n-2:
        path2 = path[:]
        arr2 = arr[:]
        # print(*path)
        while len(arr2) > 2:
            x = path2.index(min(path2))+1
            max_v += arr2[x-1] * arr2[x+1]
            arr2.pop(x)
            path2.remove(min(path2))

            # print(arr2)
            # print(path2)
        if rlt < max_v:
            rlt = max_v
        return

    for num in range(1, n-1):
        if num in path:
            continue
        path[cnt] = num

        backtracking(cnt + 1)

        path[cnt] = 0

backtracking(0)

print(rlt)