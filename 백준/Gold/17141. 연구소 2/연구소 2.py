# 17141 연구소2

import sys
input = sys.stdin.readline
from collections import deque
from itertools import combinations
# n : 연구소의 크기
# m : 놓을 수 있는 바이러스의 개수
n, m = map(int, input().strip().split())
'''
0은 빈 칸
1은 벽
2는 바이러스를 놓을 수 있는 칸
바이러스는 상하좌우로 인접한 모든 빈 칸으로 동시에 복제

연구소의 모든 빈 칸에 바이러스가 있게 되는 최소 시간을 출력
바이러스를 어떻게 놓아도 모든 빈 칸에 바이러스를 퍼뜨릴 수 없는 경우에는 -1을 출력
'''
arr = [list(map(int, input().strip().split())) for _ in range(n)]
# bfs이용
q = deque()
q2 = deque()


# q에서 m개를 골라야 함..
result = 999999999999999999
def bfs(s):
    global result
    max_val = 0
    visited2 = [[0] * n for _ in range(n)]
    for i in range(n):
        for j in range(n):
            if arr[i][j] == 1:
                visited2[i][j] = -1
    # q2.append(s)
    S = s[:]
    for i in range(m):
        visited2[S[i][0]][S[i][1]] = 1
    dx = [-1, 1, 0, 0]
    dy = [0, 0, 1, -1]
    while S:
        x, y = S.pop(0)
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < n and 0<= ny < n and visited2[nx][ny]== 0 and arr[nx][ny]!=1:
                visited2[nx][ny] = visited2[x][y] + 1
                max_val = max(visited2[nx][ny], max_val)
                S.append([nx, ny])
    ch = True
    for i in range(n):
        for j in range(n):
            if visited2[i][j] == 0:
                q2.append(1)
                ch = False
                break
        if ch is False:
            break
    if ch is True:
        result = min(result, max_val)
    return


for i in range(n):
    for j in range(n):
        if arr[i][j] == 2:
            q.append([i, j])
check = 0
if __name__ == '__main__':
    for i in combinations(q, m):
        k = list(i)
        bfs(k)
        check += 1

if len(q2)==check:
    print(-1)
elif result == 0:
    print(0)
else:
    print(result-1)

