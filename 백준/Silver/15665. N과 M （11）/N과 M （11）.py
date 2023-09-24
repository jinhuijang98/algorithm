import sys
input = sys.stdin.readline

'''
같은 수를 여러 번 골라도 된다.
'''
n, m = map(int, input().strip().split())

arr = list(map(int, input().strip().split()))
arr.sort()
path = [0] * m

def backtracking(cnt):
    if cnt == m:
        print(*path)
        return

    remember = 0
    for i in range(n):
        if remember != arr[i]:
            path[cnt] = arr[i]
            remember = arr[i]

            backtracking(cnt +1)
            # 초기화
            path[cnt] = 0

backtracking(0)