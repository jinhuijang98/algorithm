# 14562 태권왕

import sys
from collections import deque
input = sys.stdin.readline


'''
1. A는 현재 점수만큼 점수를 얻을 수 있는 엄청난 연속 발차기. 상대 역시 3점 득점하는 위험
2. B는 1점을 얻는 연속 발찿기
S와 T가 같아지는 최소 연속 발차기 횟수
1 <= s < t <= 100
'''

c = int(input().strip())

for _ in range(c):
    s, t = map(int, input().strip().split())
    q = deque()
    q.append([s, t, 0])
    # print(q)
    # visited = []
    # visited.append([s, 0])
    check = True
    while q and check is True:
        k = q.popleft()
        # print(k)
        x, y, cnt = k[0], k[1], k[2]
        # print(x, y)
        for i in range(2):
            if i == 0:
                nx = x * 2
                ny = y + 3
                ncnt = cnt + 1
                if nx > ny:
                    continue
                q.append([nx, ny, ncnt])
                if nx == ny:
                    print(ncnt)
                    check = False
                    break
                # 아직 방문하지 않았다면 append & visited에 추가 이걸 어떻게 하지
            else:
                nx = x + 1
                ny = y
                ncnt = cnt + 1
                if nx > ny:
                    continue
                q.append([nx, ny, ncnt])
                if nx == ny:
                    print(ncnt)
                    check = False
                    break






