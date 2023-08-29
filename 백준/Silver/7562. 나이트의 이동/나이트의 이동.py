import sys
input = sys.stdin.readline

def bfs(sx, sy):
    global cnt
    q = []
    q.append([sx, sy])
    visited = [[0]*l for _ in range(l)]     # 방문 확인
    visited[sx][sy] = 1                          # 시작점 1로 하기
    while q:
        x, y = q.pop(0)
        # min_len = 1000000
        for i in range(8):
            if 0<= x+dx[i] < l and 0<=y+dy[i] <l and visited[x+dx[i]][y+dy[i]] == 0:    # 범위 안에 있으면서 아직 방문하지 않았다면
                # nx, ny가 이동할 값
                visited[x+dx[i]][y+dy[i]] = visited[x][y] + 1
                q.append([x+dx[i], y+dy[i]])
            if nx == x+dx[i] and ny == y+dy[i]:
                return visited[x+dx[i]][y+dy[i]]-1




T = int(input().strip())
for tc in range(T):
    l = int(input().strip())
    # 체스판의 크기는 l x l
    x, y = map(int, input().strip().split())
    nx, ny = map(int, input().strip().split())

    # 체스판 만들기
    chess = [[0]*l for _ in range(l)]
    # 현재 위치 1로 설정
    chess[x][y] = 1
    # 나이트가 이동할 수 있는 칸
    dx = [-2, -2, -1, -1, 2, 2, 1, 1]
    dy = [-1, 1, -2, 2, -1, 1, -2, 2]
    cnt = 0
    if x == nx and y == ny:
        print(0)
    else:
        print(bfs(x, y))