# 2410 2의 멱수의 합

import sys

input = sys.stdin.readline

'''
어떤 자연수 N을 2의 멱수의 합으로 나타내는 경우의 수를 구하는 프로그램
2의 멱수라는 것은, 2^k으로 표현되는 자연수 의미


N이 홀수일 때 가능한 2의 멱수 조합의 수는 N-1의 가능한 2의 멱수 조합 수와 같고,
N이 짝수일 때 가능한 2의 멱수 조합의 수는 N-1의 가능한 2의 멱수 조합 수와 N/2의
가능한 2의 멱수의 조합의 수를 더하면 됨

ex) N이 4인 경우, N=3일 때의 조합 (1+1+1, 2+1)의 끝에 1씩 더하여 만들고,
N=2일 때의 조합 (1+1,2)에 2를 곱하여 (2+2, 4)를 만든다 => 4가지 경우의 수
1, 2, 3, 4, 5, 6, 7
1, 2, 2, 4, 4, 6, 6, 
'''

'''
10 => 14
8 + 2
8 + 1 + 1
4 + 4 + 2
4 + 4 + 1 + 1
4 + 2 + 2 + 2 
4 + 2 + 2 + 1 + 1
4 + 2 + 1 + 1 + 1 + 1
4 + 1 + 1 + 1 + 1 + 1 + 1
2 + 2 + 2 + 2 + 2
2 + 2 + 2 + 2 + 1 + 1
2 + 2 + 2 + 1 + 1 + 1 + 1
2 + 2 + 1 + 1 + 1 + 1 + 1 + 1
2 + 1 + 1 + 1 + 1 + 1 + 1 + 1 + 1
1 + 1 + 1 + 1 + 1 + 1 + 1 + 1 + 1 + 1

'''
n = int(input().strip())

dp = [1] * (n+1)

for i in range(1, n+1):
    if i % 2 == 1:
        dp[i] = dp[i-1] % 1000000000
    else:
        dp[i] = (dp[i-1] + dp[i//2]) % 1000000000

print(dp[n])