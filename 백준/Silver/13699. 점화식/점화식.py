import sys
input = sys.stdin.readline

n = int(input().strip())
dp = [0] * (n+1)

for i in range(n+1):
    if i == 0:
        dp[i] =1
    if i > 0:
        for j in range(n):
            # print(dp[j])
            # print(dp[i-1-j])
            dp[i] += dp[j] * dp[i-1-j]
print(dp[n])
