

T = int(input())

for tc in range(1, T+1):
    N, M = map(int, input().split())
    # arr의 초기값 0으로 넣음
    arr = [list(map(int, input().split())) for _ in range(N)]
    # print(arr)
    # 최대값
    max_total = 0
    for i in range(0, N):
        for j in range(0, N):
            total = 0
            for k in range(0, M):
                for l in range(0, M):
                    if 0<= i+k <=N-1 and 0<=j+l <=N-1:
                        total += arr[i+k][j+l]
            if max_total <total :
                max_total = total
    print(f'#{tc} {max_total}')

