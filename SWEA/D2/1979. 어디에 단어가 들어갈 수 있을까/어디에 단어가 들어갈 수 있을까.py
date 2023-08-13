T = int(input())
for tc in range(1, T+1):
    N, K = map(int, input().split())
    # 초기 배열
    arr =[[0]*N for _ in range(N)]
    for i in range(N):
        arr[i] = list(map(int, input().split()))

    # 최종 K의 값이 몇번 나오는지 저장할
    result = 0
    # 열 방향 먼저 탐색
    for i in range(N):
        # 1의 개수를 셀 cnt_c
        cnt_c = 0
        for j in range(N):
            if arr[i][j] == 1:
                cnt_c += 1
                if (cnt_c == K and j == N-1) or (
                    cnt_c == K and arr[i][j + 1] == 0
                ):
                    result += 1
            else:
                cnt_c = 0
    # 행 방향 탐색
    for i in range(N):
        # 1의 개수를 셀 cnt_r
        cnt_r = 0
        for j in range(N):
            if arr[j][i] == 1:
                cnt_r += 1
                if (cnt_r == K and j == N-1) or (
                    cnt_r == K and arr[j+1][i] == 0
                ):
                    result += 1
            else:
                cnt_r = 0
    print(f'#{tc} {result}')