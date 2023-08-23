n, m = map(int, input().split())

arr = [i for i in range(n)]

adj = [[0]*n for _ in range(n)]
# print(adj)

# 루트를 0으로 가정
# 간선의 수는 무조건 n-1
for i in range(1, m+1):
    adj[0][i] = 1


if (n-1) != m:
    for i in range(1, 1 + n-m-1):
        adj[i][i+m] = 1

for i in range(n):
    for j in range(n):
        if adj[i][j] == 1:
            print(i, j)