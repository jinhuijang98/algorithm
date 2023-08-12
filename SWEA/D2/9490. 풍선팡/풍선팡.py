T = int(input())

for tc in range(1, T+1):
    N, M = map(int, input().split())
    # N * M 행렬 만들기
    arr = [[0]*M for _ in range(N)]
    for i in range(N):
        arr[i] = list(map(int, input().split()))
    # 상, 하, 좌, 우로 움직이는 델타
    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]
    # 그 값만큼 추가로 터짐
    # 최대값 초기화 해놓고 시작
    max_v = 0
    for i in range(N):
        for j in range(M):
            # 그 값,,, 움직일 범위의 값 = x
            x = arr[i][j]
            # i, j에서의 터지는 꽃가루의 개수
            rlt = arr[i][j]
            for k in range(x):
                for l in range(4):
                    if 0 <= (i+(dx[l])*(k+1)) <= N-1 and 0 <= (j+(dy[l])*(k+1)) <= M-1:
                        rlt += arr[i+(dx[l])*(k+1)][j+(dy[l])*(k+1)]
            if max_v < rlt:
                max_v = rlt
    print(f'#{tc} {max_v}')