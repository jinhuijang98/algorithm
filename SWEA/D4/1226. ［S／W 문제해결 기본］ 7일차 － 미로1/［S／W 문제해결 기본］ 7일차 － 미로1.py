# 16x16 행렬
# 흰색 = 0 = 길 / 노란색 = 1 = 벽


# 출발점을 찾는 함수
def find_two():
    for i in range(16):
        for j in range(16):
            if maze[i][j] == 2:
                # i, j : 출발점
                return i, j


# bfs
def bfs(s):     # s: 시작 위치
    dx = [-1, 1, 0, 0]  # 델타 탐색
    dy = [0, 0, 1, -1]
    q = []      # 위치를 담을 q
    q.append(s)     # 시작 위치를 먼저 append
    visited[s[0]][s[1]] = 1     # 시작 위치의 값을 먼저 1로 바꿔주고 시작
    while q:        # q가 종료 됐다면 모든 탐색이 끝났다는 의미이므로
        x, y = q.pop(0)         # 시작 위치 x, y
        # 델타 탐색 시작
        for k in range(4):
            nx = x + dx[k]
            ny = y + dy[k]
            if 0 <= nx < 16 and 0 <= ny < 16:
                if maze[nx][ny]!= 1 and visited[nx][ny] == 0:
                    q.append((nx, ny))
                    visited[nx][ny] = visited[x][y] + 1
                if maze[nx][ny] == 3:
                    return 1
    return 0





# 2는 출발점, 3은 도착점
for _ in range(1, 11):
    T = int(input())
    # 미로를 받아옴 16x16
    maze = [list(map(int, input())) for _ in range(16)]
    # print(maze)
    # visited 행렬 미로 형식으로 받기
    visited = [[0]*16 for _ in range(16)]
    print(f'#{T} {bfs(find_two())}')