import sys
input = sys.stdin.readline

# 나이트가 이동할 수 있는 칸
dx = [-2, -2, -1, -1, 2, 2, 1, 1]
dy = [-1, 1, -2, 2, -1, 1, -2, 2]
# 체스판 [0,0] ~ [5,5]로 변경
col = {'A' : 0, 'B' : 1, 'C':2, 'D':3, 'E':4, 'F':5}
row = {'6' : 0, '5' : 1, '4': 2, '3': 3, '2' : 4, '1' : 5, '0' : 6}

arr = []
for _ in range(36):
    x = input().strip()
    arr.append(x)


cnt = 0
visited = [[0]*6 for _ in range(6)]
for i in range(36):
    # 현재 위치
    # print(arr[i][0])
    # print(arr[i][1])
    x = row[arr[i][1]]
    y = col[arr[i][0]]
    visited[x][y] = 1
    # print(x)
    # print(y)
    if i+1 < 36:
        nx = row[arr[i + 1][1]]
        ny = col[arr[i + 1][0]]
        for j in range(8):
            if visited[nx][ny] == 1:
                cnt = 0
                break
            elif x + dx[j] == nx and y + dy[j] == ny and visited[nx][ny] == 0:
                cnt += 1
                break
        else:
            cnt = 0
            break
    else:
        nx = row[arr[0][1]]
        ny = col[arr[0][0]]
        for j in range(8):
            if x + dx[j] == nx and y + dy[j] == ny:
                cnt += 1
                break
        else:
            cnt = 0
            break
if cnt == 36:
    print("Valid")
else:
    print("Invalid")