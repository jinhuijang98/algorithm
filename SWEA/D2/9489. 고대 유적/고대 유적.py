T = int(input())

for tc in range(1, T+1):
    N, M = map(int, input().split())
    # 초기 배열 생성
    arr = [[0]*M for _ in range(N)]
    for i in range(N):
        arr[i] = list(map(int, input().split()))
    max_v = 0
    # 행 먼저 탐색
    for i in range(N):
        cnt = 0
        for j in range(M):
            if arr[i][j] == 1:
                cnt += 1
                if max_v < cnt:
                    max_v = cnt
            else:
                if max_v < cnt:
                    max_v = cnt
                cnt = 0
    for i in range(M):
        cnt_c = 0
        for j in range(N):
            if arr[j][i] == 1:
                cnt_c += 1
                if max_v < cnt_c:
                    max_v = cnt_c
            else:
                if max_v < cnt_c:
                    max_v = cnt_c
                cnt_c = 0
    print(f'#{tc} {max_v}')