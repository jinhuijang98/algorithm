# 1309 동물원
# 다시
'''
사자들은 가로로도 세로로도 붙어 있게 배치할 수 없음
0마리 -> 1
1마리 -> 2 * N
2마리 ->


'''
n = int(input())

if n == 1:
    print(3)
else:
    dp = [1] * (n+1)
    dp[1], dp[2] = 3, 7
    for i in range(3, n+1):
        dp[i] = (2*dp[i-1] + dp[i-2]) % 9901
    print(dp[n])