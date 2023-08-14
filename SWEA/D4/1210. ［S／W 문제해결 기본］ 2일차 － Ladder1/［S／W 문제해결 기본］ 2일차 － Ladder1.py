# import sys
# sys.stdin = open('1210_ladder1.txt')
# from pprint import pprint as print

for tc in range(1, 11):
    T = int(input())
    arr = [[0]*100 for _ in range(100)]
    for i in range(100):
        arr[i] = list(map(int, input().split()))
    # arr 이차원 배열 형성
    # 도착지점 찾기
    for i in range(100):
        if arr[-1][i] == 2:
            # 도착지점의 인덱스 y에 저장
            y = i
            break
            # print(y)
    # 도착지점에서 왼/오를 먼저 보고 1이 있다면 이동
    dx = [0, 0]
    dy = [-1, 1]
    # 시작 지점은
    x = 98
    # arr[x][y]
    # 도착 지점은
    # arr[0][?]
    while x > 0:
        for i in range(2):
            if 0 <= y + dy[i] <= 99:
                if arr[x][y + dy[i]] == 1:
                    arr[x][y] = 0
                    # x = x + dx[i]
                    y = y + dy[i]
                    # print(arr)
                    break
        else:
            x -= 1
    print(f'#{tc} {y}')

    # 없다면 위로 이동
