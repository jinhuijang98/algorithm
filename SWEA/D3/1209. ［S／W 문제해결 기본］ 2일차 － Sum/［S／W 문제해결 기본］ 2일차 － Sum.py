for tc in range(10):
    T = int(input())
    arr = [list(map(int, input().split())) for _ in range(100)]
    # 각 행의 합
    # 최종 결과값 = max_value
    max_value = 0
    for i in range(100):
        total_row = 0
        for j in range(100):
            total_row += arr[i][j]
        if max_value < total_row:
            max_value = total_row
    # # 각 열의 합
    for i in range(100):
        total_col = 0
        for j in range(100):
            total_col += arr[j][i]
        if max_value < total_col:
            max_value = total_col
    # 대각선의 합 1
    total_cross_1 = 0
    for i in range(100):
        total_cross_1 += arr[i][i]
    if max_value < total_cross_1:
        max_value = total_cross_1
    # 대각선의 합 2
    total_cross_2 = 0
    for i in range(100):
        total_cross_2 += arr[i][100-i-1]
    if max_value < total_cross_2:
        max_value = total_cross_2

    print(f'#{tc+1} {max_value}')