# 1915 가장 큰 정사각형
# 다시
import sys

input = sys.stdin.readline


n, m = map(int, input().strip().split())

arr = [list(map(int, input().strip())) for _ in range(n)]

dp = [[0] * m for _ in range(n)]

answer = 0
for i in range(n):
    for j in range(m):
        if i == 0 or j == 0:
            dp[i][j] = arr[i][j]
        elif arr[i][j]==0:
            dp[i][j] = arr[i][j]
        else:
            # 모두 다 1로 채워진 2x2 정사각형을 생각해보면 [i-1][j-1] 칸과 [i-1][j]칸과 [i][j-1]칸중 가장 최소인 것의 +1이 
            # 해당 칸이 정사각형 오른쪽 아래 꼭짓점일 때 최대 크기의 정사각형
            dp[i][j] = min(dp[i][j-1], dp[i-1][j], dp[i-1][j-1]) + 1
        answer = max(dp[i][j], answer)
print(answer * answer)