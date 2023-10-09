# 1303 전쟁 - 전투

import sys
input = sys.stdin.readline

# n : 가로 크기 / m : 세로 크기
n, m = map(int, input().strip().split())

arr = [list(input().strip()) for _ in range(m)]

'''
B : 파란색 (적국)
W : 흰색 (우리 팀)
'''
visited = [[0] * n for _ in range(m)]
stack = []
cnt = 0
def dfs(s1, s2):
    global cnt
    global visited
    visited[s1][s2] = 1     # 현재지점 방문 표시
    cnt += 1

    # 위 아래 양 옆
    dx = [1, -1, 0, 0]
    dy = [0, 0, 1, -1]


    # 갈 수 있는 곳들을 stack에 추가
    for i in range(4):
        nx = s1 + dx[i]
        ny = s2 + dy[i]
        if 0 <= nx < m and 0 <= ny < n:
            if visited[nx][ny] == 0:
                if arr[nx][ny] == arr[s1][s2]:
                    dfs(nx, ny)
# 당국
answer=[0,0]
for i in range(m):
    for j in range(n):
        if visited[i][j] == 0:
            cnt = 0
            if arr[i][j] == "W":
                dfs(i, j)
                answer[0] += cnt**2
            else:
                dfs(i, j)
                answer[1] += cnt ** 2
print(*answer)