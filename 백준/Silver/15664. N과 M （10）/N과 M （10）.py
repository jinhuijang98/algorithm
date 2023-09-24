import sys
input = sys.stdin.readline

n, m = map(int, input().strip().split())

arr = list(map(int, input().strip().split()))

arr.sort()
path = [0] * m
visited = [False] * n
result = []
# 그러니까 visited[]를 순차적으로 선택해야한다는겨..
# 1 7 & 7 1 중에 1 7만 나오게 이전 visited는 모두 false여야 함
def backtracking(cnt):

    if cnt == m:
        if path == sorted(path):
            print(*path)
        return
    remember = 0
    for i in range(n):
        if not visited[i] and remember != arr[i]:
            visited[i] = True
            path[cnt] = arr[i]
            remember = arr[i]
            # 다음 재귀함수 호출
            backtracking(cnt + 1)
            # 돌아와서 할 로직 => 초기화
            path[cnt] = 0
            visited[i] = False

backtracking(0)
