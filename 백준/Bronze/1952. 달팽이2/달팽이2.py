import sys
input = sys.stdin.readline


M, N = map(int, input().split())

    # 우 하 좌 상
dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]

# M * N 0으로 채운 arr 저장
arr = [[0]*N for _ in range(M)]


# 처음 (0,0)에서 우 하 좌 상 방향으로 탐색을 하는데
# 방향이 바뀐 횟수를 구함
# 처음 위치
x = 0
y = 0
# 달팽이가 이동하면서 값을 증가시키고 기록할 변수
count = 1
# 이동할 방향 표시
dir = 0
arr[x][y] = count # 시작 위치에 1을 기록

arr[0][0] = 1
# print(arr)

# 달팽이 반복 시작
total = 0
while count < N*M: # N*M만큼 판이 만들어지니까
    nx = x+dx[dir]
    ny = y+dy[dir]

    # 다음 조사 위치가 0보다 크거나 같고, N보다 작다면 / 그리고 다음 위치가 0이면
    if 0 <= nx < M and 0 <= ny < N and arr[nx][ny]==0:
        count += 1
        arr[nx][ny] = count
        x, y = nx, ny # 내 위치 갱신
    else:
        dir += 1
        total += 1
        if dir >= 4:
            dir = 0

print(total)