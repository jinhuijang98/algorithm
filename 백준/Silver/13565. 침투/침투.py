import sys
input = sys.stdin.readline

m, n = map(int, input().strip().split())
'''
검은색 => 전류 차단 (1)
흰색 => 전류 통함 (0)
전류는 섬유 물질의 가장 바깥쪽 흰색 격자(0행) 들에 공급 
상하좌우 인접한 흰색 격자로 전달
바깥쪽에서 흘려준 전류가 안쪽(m행)까지 침투될 수 있는지 아닌지를 판단

'''
arr = [list(map(int, input().strip())) for _ in range(m)]

def bfs(s1, s2):
    global check
    visited = [[0] * n for _ in range(m)]

    q = []
    q.append([s1, s2])
    visited[s1][s2] = 1
    dx = [1, -1, 0, 0]
    dy = [0, 0, 1, -1]
    while q:
        x, y = q.pop(0)

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if nx == m-1 and 0<=ny<n and visited[nx][ny] == 0 and arr[nx][ny]==0:
                check = True
                return
            if 0<= nx < m and 0<=ny<n and visited[nx][ny] == 0 and arr[nx][ny]==0:
                q.append([nx, ny])
                visited[nx][ny] = 1
    return

for j in range(n):
    check = False
    if arr[0][j] == 0:
        bfs(0, j)
        if check is True:
            print("YES")
            break
else:
    print("NO")
