T = int(input())
# from pprint import pprint
# 초기값으로 0을 100x100 넣은 arr 만듦
arr = [[0]*100 for _ in range(100)]
# pprint(arr)

for tc in range(1, T+1):
    # N과 M 값을 가져옴
    N, M = map(int, input().split())
    # 기존의 넓이는 100*N
    # 기존의 넓이에서 겹치는 영역의 길이 재서 빼기
    for i in range(10):
        for j in range(10):
            arr[N+i][M+j] += 1
    # 넓이
    con = 0
    for i in range(100):
        for j in range(100):
            if arr[i][j] >= 1:
              con += 1



print(con)