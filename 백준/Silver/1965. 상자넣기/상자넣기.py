# 1965 상자넣기

import sys

input = sys.stdin.readline


'''
dp이용..

'''
n = int(input().strip())

arr = list(map(int, input().strip().split()))

dp = [1] * n

for i in range(0, n):

    # 만약 arr[i]가 arr[i-1]보다 크다면 상자에 담을 수 있으므로 +1
    for j in range(i-1, -1, -1):
        if arr[i] > arr[j] and dp[i] < dp[j] + 1:
            dp[i] = dp[j] + 1
        # else:
        #     dp[i] = max(dp[:j]) + 1
print(max(dp))