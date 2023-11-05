from sys import stdin
input = stdin.readline

dr = (1, 0, -1, 0)
dc = (0, 1, 0, -1)

def dfs(depth, r, c, char, gr, gc):
    if (r, c) == (gr, gc) and depth >= 4:
        print("Yes")
        exit()

    for d in range(4):
        nr = r + dr[d]
        nc = c + dc[d]
        # 격자 밖이거나 다른 문자이면
        if not (0 <= nr < R and 0 <= nc < C) or board[nr][nc] != char:
            continue
        # 방문할 수 있다면
        if not check[nr][nc]:
            check[nr][nc] = 1		# 방문 표시
            dfs(depth+1, nr, nc, board[nr][nc], gr, gc)
            check[nr][nc] = 0		# 복원

# main
R, C = map(int, input().split())
board = [list(input().rstrip()) for _ in range(R)]
check = [[0] * C for _ in range(R)]
for sr in range(R):
    for sc in range(C):
        dfs(0, sr, sc, board[sr][sc], sr, sc)
print("No")