import sys
input = sys.stdin.readline

N = int(input())
stone = []

# dp 배열 생성
dp = [1e9]*N
dp[0] = 0
for i in range(N-1):
    s, b = map(int, input().split())
    stone.append((s, b))
    if i+1<N : dp[i+1] = min(dp[i+1], dp[i]+s)
    if i+2<N : dp[i+2] = min(dp[i+2], dp[i]+b)

# 매우 큰 점프 적용해보며 최솟값 찾기
K = int(input())
_min = dp[-1]
for i in range(3, N):
    e, dp1, dp2 = dp[i-3]+K, 1e9, 1e9
    for j in range(i, N-1):
        if i+1<=N : dp1 = min(dp1, e+stone[j][0])
        if i+2<=N : dp2 = min(dp2, e+stone[j][1])
        e, dp1, dp2 = dp1, dp2, 1e9
    _min = min(_min, e)

print(_min)