T = int(input())
for tc in range(T):
    k = int(input())
    n = int(input())
    # k층 n호 층은 0부터 호는 1부터
    arr = [[0]*n for _ in range(k+1)]
    # print(arr)
    # 0층의 값 채움
    for i in range(n):
        arr[0][i] = i+1

    # a층의 b호에 살려면 자신의 아래 (a-1)층의 1호부터 b호까지 사람들의 수의 합만큼
    # arr[i][j] = arr[i-1][0] + arr[i-1][1] + ... + arr[i-1][j]
    for i in range(1, k+1):
        for j in range(n):
            if j == 0:
                # 0행은 1로 채움
                arr[i][j] = 1
            else:
                # 1행부터는 값 더해주면서 채우기
                for l in range(j+1):
                    arr[i][j] += arr[i - 1][l]
            # arr[i][j] += arr[i-1][j]

    print(arr[k][n-1])