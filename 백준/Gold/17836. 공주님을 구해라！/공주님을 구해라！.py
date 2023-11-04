import sys
from collections import deque
input = sys.stdin.readline
N, M, T = map(int,input().split())
dx, dy = [-1, 1, 0, 0], [0, 0, -1, 1]
m = [list(map(int,input().split())) for _ in range(N)]
q = deque()
visited = [[0] * M for _ in range(N)]
 
def bfs():
    gram = 10001
    q.append((0, 0))
    visited[0][0] = 1
    while q:
        x, y = q.popleft()
        # 공주님이 있는 곳에 도착했을 때
        if (x, y) == (N-1, M-1):
            return min(visited[x][y]-1, gram)
        # 그람이 있는 곳에 도착했을 때
        if m[x][y] == 2:
            gram = visited[x][y]-1 + N-1-x + M-1-y
 
        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]
            if 0 <= nx < N and 0 <= ny < M and not visited[nx][ny]:
                if m[nx][ny] == 0 or m[nx][ny] == 2:
                    visited[nx][ny] = visited[x][y] + 1
                    q.append((nx, ny))
    return gram
 
res = bfs()
if res > T:
    print('Fail')
else:
    print(res)