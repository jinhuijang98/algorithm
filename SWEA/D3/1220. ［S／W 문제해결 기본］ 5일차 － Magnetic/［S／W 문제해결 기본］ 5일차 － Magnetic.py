for tc in range(1, 11):
    # 테이블의 크기 : 항상 100
    N = int(input())
    # 100 x 100 초기배열
    arr = [list(map(int, input().split())) for _ in range(N)]
    # 1은 N극 성질, 2는 S극 성질
    # 테이블 윗부분은 N극, 아래부분 S극
    # 자성체는 테이블 앞뒤 쪽에 있는 N극 또는 S극 에만 반응
    cnt = 0
    for i in range(N):
        for j in range(N):
            x = j       # 행
            y = i       # 열
            if arr[j][i] == 1:
                if j == N-1:
                    arr[j][i] =0
                while x+1 < N and arr[x+1][y] != 2:
                    # 2가 아니라면 값을 위아래 바꿔줌
                    arr[x][y], arr[x+1][y] = arr[x+1][y], arr[x][y]
                    x += 1
                    if x == N-1:
                        arr[x][y] = 0
            if arr[j][i] == 2:
                if j == 0:
                    arr[j][i] = 0
                while 0 <= x-1 and arr[x-1][y] != 1:
                    arr[x-1][y], arr[x][y] = arr[x][y], arr[x-1][y]
                    x -= 1
                    if x == 0:
                        arr[x][y] = 0

    for i in range(N):
        for j in range(N):
            # 열 탐색하면 제일 위에 있는 값이 무조건 1
            # j는 무조건 마지막 행이 될 수 없음
            if arr[j][i] == 1 and arr[j+1][i] == 2:
                cnt += 1


    print(f'#{tc} {cnt}')

