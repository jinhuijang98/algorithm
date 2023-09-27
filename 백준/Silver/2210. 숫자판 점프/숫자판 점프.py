arr = [list(input().split()) for _ in range(5)]

result = []
def dfs(x, y, number):
    if len(number)== 6:
        if number not in result:
            result.append(number)
        return

    dx = [1, -1, 0, 0]
    dy = [0, 0, 1, -1]
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if 0 <= nx < 5 and 0<= ny < 5:
            dfs(nx, ny, number+arr[nx][ny])

# dfs(3,3, arr[3][3])
for j in range(5):
    for k in range(5):
        dfs(j, k, arr[j][k])
print(len(result))