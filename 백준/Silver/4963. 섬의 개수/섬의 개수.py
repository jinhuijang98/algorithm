import sys
input = sys.stdin.readline


def delta(x, y):
    dx = [1, 0, -1, 0, -1, -1, 1, 1]
    dy = [0, 1, 0, -1, -1, 1, 1, -1]
    stack = []
    # arr[y][x] == 1인 위치를 stack에 저장
    stack.append([x, y])
    # 우선 지금 있는 값을 0으로 바꾸고
    # arr[y][x] = 0
    # stack에 값이 존재하는 동안 반복문
    while stack:
        # 먼저 꺼내서 0으로 바꾸기
        x, y = stack.pop()
        arr[y][x] = 0
        # 상하좌우 움직이며
        for i in range(8):
            nx = x + dx[i]
            ny = y + dy[i]
            # 인덱스 범위 안에 존재한다면
            if 0 <= nx < w and 0 <= ny < h:
                # 그리고 값이 1이라면
                if arr[ny][nx] == 1:
                    # 그 위치를 stack에 저장
                    stack.append([nx, ny])
        else:
            continue
    return


# T = int(input())
check = True
while check:
    w, h = list(map(int, input().split()))
    if w == 0 and h == 0:
        check = False
        break
    else:
        arr = [[0] * w for _ in range(h)]
        # print(arr)
        if w == 1 and h == 1:
            result = int(input())
            # result = 0
        else:
            for i in range(h):
                arr[i] = list(map(int, input().split()))
            result = 0
            for i in range(h):
                for j in range(w):
                    if arr[i][j] == 1:
                        result += 1
                        delta(j, i)
    print(result)

#