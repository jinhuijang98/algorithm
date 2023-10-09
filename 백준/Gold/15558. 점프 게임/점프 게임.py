# 15558 점프게임

import sys
input = sys.stdin.readline


# n개의 칸
# 각 칸은 안전한 칸 or 위험한 칸
'''
안전한 칸 : 유저가 이동할 수 있는 칸 (1)
위험한 칸 : 이동할 수 없는 칸 (0)
왼쪽 줄의 1번 칸 위에서 매 초마다
1. 한 칸 앞으로 이동한다. 예를 들어, 현재 있는 칸이 i번 칸이면, i+1번 칸으로 이동
2. 한 칸 뒤로 이동한다. 예를 들어, 현재 있는 칸이 i번 칸이면, i-1번 칸으로 이동
3. 반대편 줄로 점프한다. 이때, 원래 있던 칸보다 k칸 앞의 칸으로 이동해야 한다. 예를 들어, 현재 있는 칸이 왼쪽 줄의 i번 칸이면, 오른쪽 줄의 i+k번 칸으로 이동
이 세가지 중 하나

n번 칸보다 큰 칸으로 이동하는 경우 게임 클리어
1초에 한 칸씩 각 줄의 첫 칸이 사라지는 기능
1초가 지나면 1번 칸이 없어지고 2초가 지나면 2번 칸이 없어지고....
유저가 움직이고, 칸이 사라진다고 가정
게임을 클리어할 수 있으면 1
없으면 0
'''
n, k = map(int, input().strip().split())

arr = [list(map(int, input().strip())) for _ in range(2)]
'''
[0, 0]에서 시작

'''
visited = [[0] * n for _ in range(2)]
cnt = 0
check = False
def bfs(s1, s2):
    global cnt
    global check
    # cnt = 0
    q = []
    visited[s1][s2] = 1
    q.append([s1, s2])
    # x는 행방향
    # y는 열방향
    dx = [0, 0, 1, -1]
    dy = [1, -1, k, k]
    while q:
        x, y = q.pop(0)
        # 행 번호랑 visited 비교
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < 2 and ny > n-1:
                check = True
                return
            if 0 <= nx < 2 and 0 <= ny < n:
                if visited[nx][ny] == 0 and arr[nx][ny] == 1 and ny >= visited[x][y]:
                    q.append([nx, ny])
                    visited[nx][ny] = visited[x][y] + 1

    return

bfs(0,0)
if check is True:
    print(1)
else:
    print(0)