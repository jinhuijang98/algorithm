import sys

n, m = map(int, sys.stdin.readline().split())
DP = [[[0,[True,True]] for _ in range(m+1)] for _ in range(n+1)]
DP[0][0][0] = 1

k = int(sys.stdin.readline())
for _ in range(k):
    a,b,c,d = map(int, sys.stdin.readline().split())
    if a > c: a, c = c, a
    if b > d: b, d = d, b
    d = 0 if c-a> d-b else 1
    DP[a][b][1][d] = False
   
moves = [(1,0), (0,1)] 
for x in range(n+1):
    for y in range(m+1):
        for i in range(2):
            nx, ny = x + moves[i][0], y + moves[i][1]
            if nx <= n and ny <= m and DP[x][y][1][i]:
                DP[nx][ny][0] += DP[x][y][0]
                
print(DP[n][m][0])