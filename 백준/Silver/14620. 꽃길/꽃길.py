import sys
from itertools import combinations

def check(li):
    global answer
    visited = [] # 꽃잎이 서로 닿지 않는지 확인
    total = 0 # 꽃을 피울 때 해당 좌표의 대여비용을 합할 변수
    for r, c in li:
        visited.append((r, c)) # 꽃의 중앙 좌표를 먼저 담는다
        total += fields[r][c] # 꽃의 중앙 좌표의 대여비를 초기값으로 잡는다.
        for idx in range(4): # 중앙으로부터 인접한 4방향 칸을 확인한다.
            nr = r + d[idx][0]
            nc = c + d[idx][1]
            if (nr, nc) not in visited:
                visited.append((nr, nc))
                total += fields[nr][nc]
            else: # 꽃잎이 서로 닿게되는 경우는 함수를 종료한다.
                return
    answer = min(answer, total) # 모든 꽃을 피울 수 있다면 최소 비용으로 최신화한다.

d = [(-1, 0), (1, 0), (0, -1), (0, 1)]

N = int(input())
answer = int(1e9)
fields = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]
candidates = [(r, c) for r in range(1, N-1) for c in range(1, N-1)]

for li in combinations(candidates, 3):
    check(li)
print(answer)