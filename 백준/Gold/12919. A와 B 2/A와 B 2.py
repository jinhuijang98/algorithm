# bfs 와 델타 탐색 델타를 두 가지 동작이라 생각하고

from collections import deque
import sys

s = input()
t = input()

# t에서 빼는 걸로
def bfs(s, t):
    q = deque()
    q.append(t)
    while q:
        t = q.popleft()
        if t==s:
            return 1
        if 1 < len(t):
            for i in range(1, 3):
                if i % 2:
                    if t[-1] == 'A':
                        x = t[:-1]
                        q.append(x)
                else:
                    if t[0] == 'B':
                        x = t[::-1]
                        x = x[:-1]
                        q.append(x)

    return 0

print(bfs(s, t))
