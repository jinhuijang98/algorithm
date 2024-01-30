# 5567 결혼식
import sys
from collections import deque
input = sys.stdin.readline

# 상근이의 동기 수 (상근이는 1번)
n = int(input().strip())

# 리스트의 길이
m = int(input().strip())

adj = [[] for _ in range(n+1)]
cnt = 0
for i in range(m):
    a, b = map(int, input().strip().split())
    adj[a].append(b)
    adj[b].append(a)


def bfs(start):
    global cnt
    q = deque()
    q.append(start)
    visited = [0] * (n+1)
    visited[start] = 1
    while q:
        x = q.popleft()
        for i in range(len(adj[x])):
            nx = adj[x][i]
            if not visited[nx]:
                visited[nx] = visited[x] + 1
                if visited[nx] == 2 or visited[nx] == 3:
                    cnt += 1
                q.append(nx)
    return cnt

print(bfs(1))
