import sys
input = sys.stdin.readline

def dfs(x, y, z):
    global answer
    visited = arr[x][y]

    # 반복문을 통해 종이를 확인
    for i in range(x, x+z):
        for j in range(y, y+z):
            # 시작점의 종이의 색깔과 현재 종이의 색깔이 다르다면
            if arr[i][j] != visited:
                # 재귀로 탐색
                for k in range(0, z//2+1, z//2):
                    for l in range(0, z//2+1, z//2):
                        dfs(x + k, y + l, z//2)
                return

    if visited == 0:
        answer[0] += 1
    else:
        answer[1] += 1


n = int(input().strip())
arr = [list(map(int, input().strip().split())) for _ in range(n)]
answer = [0, 0]
dfs(0, 0, n)
print(answer[0])
print(answer[1])