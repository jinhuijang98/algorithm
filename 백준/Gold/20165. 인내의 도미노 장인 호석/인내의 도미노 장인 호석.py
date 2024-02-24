# 20165 인내의 도미노 장인 호석
'''
너 죽고 나 살자 게임
2명이 공격과 수비.
공격수는 도미노를 계속 넘어뜨리고 수비수는 도미노를 계속 세움
1. N행 M열의 2차우너 격자 모양의 게임판의 각 격자에 도미노를 세움. 각 도미노는 1 이상 5 이하의 높이를 가짐
2. 매 라운드는 공격수가 먼저 공격하고, 수비수는 공격이 끝난 뒤에 수비
3. 공격수는 특정 격자에 놓인 도미노를 동, 서, 남, 북 중 원하느 방향으로 넘어뜨림. 길이가 k인 도미노가 특정 방향으로 넘어진다면,
그 방향으로 k-1개의 도미노들 중 아직 넘어지지 않은 것들이 같은 방향으로 연달아 넘어짐.
도미노의 특성상, 연쇄적으로 도미노가 넘어질 수 있음. 이미 넘어진 도미노가 있는 칸을 공격한 경우에는 아무 일이 일어나지 않음.
4. 


'''


from sys import stdin
from collections import deque

input = stdin.readline
dir = {
    'E':[0,1],
    'W':[0,-1],
    'N':[-1,0],
    'S':[1,0]
}

n,m,r = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(n)]
orders = []
status_board = [['S'] * m for _ in range(n)]
for _ in range(r):
    order = []
    x,y,d = input().split()
    order.append((int(x)-1,int(y)-1,d))

    x,y = map(int, input().split())
    order.append((x-1,y-1))
    orders.append(order)
def solv():
    score = 0
    for order in orders:
        ax,ay,d = order[0]
        if status_board[ax][ay] == 'S':
            score += attack(ax,ay,d)

        dx,dy = order[1]
        if status_board[dx][dy] == 'F':
            defense(dx,dy)

    print(score)
    for row in status_board:
        print(*row)
def attack(sx,sy,d):
    global status_board
    q = deque([(sx,sy)])
    status_board[sx][sy] = 'F'
    score = 0
    while q:
        x,y = q.pop()
        cnt = board[x][y]
        score += 1
        for _ in range(cnt-1):
            x += dir[d][0]
            y += dir[d][1]

            if not point_validator(x,y):
                break
            if status_board[x][y] == 'S':
                status_board[x][y] = 'F'
                q.appendleft((x,y))
    return score
def defense(x,y):
    global status_board
    status_board[x][y] = 'S'

def point_validator(x,y):
    if x < 0 or y < 0 or x >= n or y >= m:
        return False
    return True
solv()