n, m, k = map(int, input().split())
# n : 행의 수, m : 열의 수, k : 0으로 표시된 칸의 번호
'''
k가 0인 경우도 존재
이 경우 1 => n*m으로 이동
'''

# 1 ~ n까지 1행
# n+1 ~ 2n 까지 2행
# ...
# n*m까지   m행


fin_a = []
for i in range(0, m*n, m):
    a = []
    for j in range(m):
        a.append(i+1+j)
    fin_a.append(a)
# print(fin_a)

if k != 0:
    # k가 0이 아닐 때 행과 열을 x, y에 저장
    check = False
    for i in range(n):
        for j in range(m):
            if fin_a[i][j] == k:
                x, y = i, j
                check = True
                break
        if check is True:
            break

    arr = [[0] * (y+1) for _ in range(x+1)]
    for i in range(x+1):
        for j in range(y+1):
            if i == 0 or j == 0:
                arr[i][j] = 1
            else:
                arr[i][j] = arr[i - 1][j] + arr[i][j - 1]
    first = arr[x][y]
    # print(first)
    # 전체 크기를 (n) * (m)로 잡아야 함
    # n-(x+1)+1
    # n-x
    arr2 = [[0] * (m-y) for _ in range(n-x)]
    for i in range(n-x):
        for j in range(m-y):
            if i == 0 or j == 0:
                arr2[i][j] = 1
            else:
                arr2[i][j] = arr2[i - 1][j] + arr2[i][j - 1]
    second = arr2[n-x-1][m-y-1]
    print(first * second)

else:
    arr = [[0] * m for _ in range(n)]
    # print(arr)
    for i in range(n):
        for j in range(m):
            if i == 0 or j == 0:
                arr[i][j] = 1
            else:
                arr[i][j] = arr[i - 1][j] + arr[i][j - 1]
    first = arr[n-1][m-1]
    print(first)


'''
k == 0일때에는 1-> n*m
k!=0 일때에는 1-> k -> n*m으로 bfs 이동
'''
