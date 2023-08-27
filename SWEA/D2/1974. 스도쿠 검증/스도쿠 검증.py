
'''
1. 행탐색
2. 열탐색
3. 3 x 3 탐색
'''
'''
1 ~9까지 인덱스를 활용해서
값을 만나면 + 1 
만약 +2 가 된다면 0을 출력
그렇지 않다면 1을 출력
'''
T = int(input())
for tc in range(1, T + 1):
    # 9 x 9 스도쿠
    arr = [list(map(int, input().split())) for _ in range(9)]
    # 행
    check = True
    for i in range(9):
        idx = [0] * 10
        # 만날 때마다 +1
        for j in range(9):
            idx[arr[i][j]] += 1
            # idx[arr[j][i]] += 1
        for k in range(1, 10):
            if idx[k] == 0:
                check = False
                break
    # print(check)
    # print()
    # 열 탐색
    if check is True:
        for i in range(9):
            idx = [0] * 10
            for j in range(9):
                idx[arr[j][i]] += 1

            for k in range(1, 10):
                if idx[k] == 0:
                    check = False
                    break
    # print(check)

    if check is True:
        dx = [0, 0, 0, 1, 2, 1, 1, 2, 2]
        dy = [0, 1, 2, 0, 0, 1, 2, 1, 2]
        for i in range(0, 9, 3):
            idx = [0] * 10
            if check is True:
                for j in range(0, 9, 3):
                    for k in range(9):
                        x = arr[i+dx[k]][j+dy[k]]
                        # print(x)
                        idx[x] += 1
                    for l in range(1, 10):
                        if idx[l] == 0:
                            check = False
                            break
            else:
                break

    if check is True:
        print(f'#{tc} 1')
    else:
        print(f'#{tc} 0')




