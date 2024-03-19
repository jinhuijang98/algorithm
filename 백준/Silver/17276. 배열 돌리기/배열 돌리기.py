# 17276 배열돌리기

import sys

input = sys.stdin.readline
from copy import deepcopy
t = int(input().strip())


for tc in range(t):
    n, d = map(int, input().strip().split())
    arr = [list(map(int, input().strip().split())) for _ in range(n)]
    # 결과 저장할 배열
    result = [[0]* n for _ in range(n)]

    if d < 0:
        d += 360

    # 제자리일 경우 그대로 출력
    if d == 0 or d == 360:
        for l in arr:
            print(*l)

    else:
        # 45의 배수로 나오므로 나눈 몫만큼 반복
        for _ in range(d//45):
            for i in range(n):
                for j in range(n):
                    # 주 대각선이라면 가운데 행을 들고 와줌
                    if i == j:
                        result[i][j] = arr[n//2][j]
                    # 가운데 행이라면 부 대각선
                    elif i == n//2:
                        result[i][j] = arr[n-j-1][j]
                    # 부대각선이라면 가운데 열을 가져옴
                    elif i+j == n-1:
                        result[i][j] = arr[i][n//2]
                    # 가운데 열이라면 주 대각선을 가져옴
                    elif j == n//2:
                        result[i][j] = arr[i][i]
                    # 모두 아니라면 원래 값
                    else:
                        result[i][j] = arr[i][j]
            arr = deepcopy(result)
        for k in result:
            print(*k)


