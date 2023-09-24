import sys
input = sys.stdin.readline

n, m = map(int, input().strip().split())

arr = list(map(int, input().strip().split()))

arr.sort()

path = [0] * m

def backtracking(cnt):
    if cnt == m:
        if path == sorted(path):
            print(*path)
        return

    remember = 0
    for i in range(n):
        if remember != arr[i]:
            path[cnt] = arr[i]
            remember = arr[i]
            backtracking(cnt+1)
            path[cnt] = 0
backtracking(0)