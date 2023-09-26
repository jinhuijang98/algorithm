import sys
input = sys.stdin.readline

n, m = map(int, input().strip().split())
arr = [list(map(int, input().strip().split())) for _ in range(n)]
'''
어떤 칸의 안전 거리는 그 칸과 가장 거리가 가까운 아기 상어와의 거리
두 칸의 거리는 하나의 칸에서 다른 칸으로 가기 위해서 지나야 하는 칸의 수, 이동은 인접한 8방향
1에서 1까지의 각 거리를 bfs로 탐색하면서 가지치기
'''
total = 1000000
def bfs(s1, s2):
    global total
    q = []
    q.append([s1, s2])
    visited = [[0] * m for _ in range(n)]
    visited[s1][s2] = 1
    dx = [1, -1, 0, 0, 1, -1, 1, -1]
    dy = [0, 0, 1, -1, 1, -1, -1, 1]
    while q:
        x, y = q.pop(0)
        for i in range(8):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < n and 0 <= ny < m and visited[nx][ny] == 0:
                q.append([nx, ny])
                visited[nx][ny] = visited[x][y] + 1
                if arr[nx][ny] == 1:
                    total = visited[nx][ny]-1
                    return
result = 0
for i in range(n):
    for j in range(m):
        if arr[i][j] == 1:
            continue
        else:
            bfs(i, j)
            result = max(total, result)
print(result)