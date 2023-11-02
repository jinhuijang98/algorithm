from collections import deque

def bfs(n):
    visited = [-1] * (N+1)
    visited[n] = 0
    Q = deque([n])
    while Q:
        v = Q.popleft()
        for w in adj[v]:
            if visited[w] == -1:
                visited[w] = visited[v] + 1
                Q.append(w)
    return max(visited)

N = int(input())
adj = [[] for _ in range(N+1)]
while True:
    a, b = map(int, input().split())
    if a == -1 and b == -1:
        break
    adj[a].append(b)
    adj[b].append(a)

score = 50
lst = []

for n in range(1, N+1):
    tmp = bfs(n)
    if tmp < score:
        score = tmp
        lst = [n]
    elif tmp == score:
        lst.append(n)
print(score, len(lst))
print(*lst)