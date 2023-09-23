import sys
input = sys.stdin.readline

n, m = map(int, input().strip().split())
arr = list(map(int, input().strip().split()))
arr.sort()
path = [0]*m
result = []


visited = [False] * n
def backtracking(cnt, m):
    global result
    # 가지치기
    # 기저 조건
    # 숫자 m개를 골랐을 때 종료
    if cnt == m:
        print(*path)
        return
    # 중복 방지를 위해
    remember = 0
    for i in range(n):
        # 가지치기 - 중복된
        if not visited[i] and remember != arr[i]:
        # 들어가기 전 로직 - 경로 저장
            visited[i] = True
            path[cnt] = arr[i]
            remember = arr[i]
            # 다음 재귀 함수 호출
            backtracking(cnt + 1, m)
            # 들어와서 할 로직 (초기화)
            visited[i] = False
            path[cnt] = 0

backtracking(0, m)
for i in result:
    print(*i, end= ' ')
    print()