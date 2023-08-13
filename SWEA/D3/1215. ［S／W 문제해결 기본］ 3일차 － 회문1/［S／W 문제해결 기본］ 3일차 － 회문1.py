for tc in range(1, 11):
    N = int(input())
    arr = [['']*8 for _ in range(8)]
    for i in range(8):
        arr[i] = list(input())
    # 검사할 길이 = N

    # 열 먼저 탐색
    result = 0
    for i in range(8):
        for j in range(8-N+1):
            new_str = ''
            for k in range(N):
                new_str += arr[i][j+k]
            cnt = 0
            for l in range(N//2):
                if new_str[l] != new_str[N-l-1]:
                    break
                else:
                    cnt += 1
            if cnt == (N//2):
                result += 1
    # 행 탐색
    for i in range(8):
        for j in range(8-N+1):
            new_str = ''
            for k in range(N):
                new_str += arr[j+k][i]
            cnt = 0
            for l in range(N//2):
                if new_str[l] != new_str[N-l-1]:
                    break
                else:
                    cnt += 1
            if cnt == (N//2):
                result += 1
    print(f'#{tc} {result}')
