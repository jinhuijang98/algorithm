import sys
from collections import deque

N, M = map(int, sys.stdin.readline().split())
arr = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]

di = [1, 1, 1]
dj = [-1, 0, 1]

q = deque()
for l in range(M):
    q.append([0, l, arr[0][l], -1])  # i, j, total, direction

min_total = 99999

while q:
    i, j, total, direction = q.popleft()

    if i == N-1:
        if total < min_total:
            min_total = total

    for k in range(3):
        if direction == k:
            continue
        else:
            ni, nj = i + di[k], j + dj[k]
            total2 = total
            if 0 <= ni < N and 0 <= nj < M:
                total2 += arr[ni][nj]
                q.append([ni, nj, total2, k])


print(min_total)