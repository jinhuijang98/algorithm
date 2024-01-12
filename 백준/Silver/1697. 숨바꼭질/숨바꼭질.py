# 1697 숨바꼭질
import sys
from collections import deque
input = sys.stdin.readline

n, k = map(int, input().strip().split())

visited = [0] * 100001

q = deque()
q.append(n)

while q:
    now = q.popleft()
    
    if now == k:
        print(visited[now])
        break
    for nx in (now-1, now+1, now*2):
        if 0 <= nx < 100001 and visited[nx] == 0:
            visited[nx] = visited[now] + 1
            q.append(nx)
