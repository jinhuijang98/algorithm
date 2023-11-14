# 5582 공통 부분 문자열
import sys
input = sys.stdin.readline

s1 = list(input().strip())
s2 = list(input().strip())

len1 = len(s1)
len2 = len(s2)
# 2차원으로 dp만들기
dp = [[0] * (len(s2)) for _ in range(len(s1))]
answer = 0
for i in range(len(s1)):
    for j in range(len(s2)):
        if s1[i] == s2[j]:
            if i == 0 or j == 0:
                dp[i][j] = 1
            else:
                dp[i][j] = dp[i-1][j-1] + 1
        answer = max(dp[i][j], answer)
print(answer)