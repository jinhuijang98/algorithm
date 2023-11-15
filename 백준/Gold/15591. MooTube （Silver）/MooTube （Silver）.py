# 15591 MooTube (Silver)
from collections import deque
import sys
input = sys.stdin.readline


N, Q = map(int, input().strip().split())
graph = [[]  for _ in range(N+1)]
for _ in range(N-1):
    p, q, r = map(int, input().strip().split())
    graph[p].append([q, r])
    graph[q].append([p, r])

for i in range(Q):
    k, v = map(int, input().strip().split())
    visited = [False] * (N+1)
    visited[v] = True
    result = 0
    q = deque([(v, float('inf'))])

    while q:
        v, usado = q.popleft()
        for next_v, next_usado in graph[v]:
            next_usado = min(usado, next_usado)
            if next_usado >= k and not visited[next_v]:
                result += 1
                q.append((next_v, next_usado))
                visited[next_v] = True
    print(result)