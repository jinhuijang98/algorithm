# 1010 다리 놓기

# nCr = n!/(n-r)!r!

import sys
input = sys.stdin.readline
from itertools import combinations

T = int(input().strip())
dp = [[0] * 30 for _ in range(30)]

for i in range(30):
    for j in range(30):
        if i == 1:
            dp[i][j] = j
        else:
            if i == j:
                dp[i][j] = 1
            elif i < j:
                dp[i][j] = dp[i-1][j-1] + dp[i][j-1]


for _ in range(T):
    n, m = map(int, input().strip().split())
    print(dp[n][m])