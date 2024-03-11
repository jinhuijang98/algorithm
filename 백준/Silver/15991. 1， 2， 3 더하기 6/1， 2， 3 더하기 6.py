# 15991 1, 2, 3 더하기 6

'''
1 -> 1
2 -> 1
3 -> 1 + 1 + 1 -> 1
4 : 3
-> 1 + 1 + 1 + 1
-> 1 + 2 + 1
-> 2 + 2
5 : 2
-> 1 1 1 1 1
-> 1 3 1
6 : 4
-> 1 1 1 1 1 1
1 1 2 1 1
1 2 2 1
2 1 1 2


7 : 6 => dp[5] +
=>  3 4 => 3 2 2 => 2 3 2
1 1 1 1 1 1 1 1
2 3 2
1 1 3 1 1
3 1 3
1 1 3 1 1
1 3 1 3 1
'''

import sys
input = sys.stdin.readline

dp = [0] * (10**5 + 1)
dp[1] = 1
dp[2] = 2
dp[3] = 2
dp[4] = 3
dp[5] = 3
dp[6] = 6
dp[7] = 6

for i in range(8, 10**5 + 1):
    dp[i] = dp[i - 2] + dp[i - 4] + dp[i - 6]

for _ in range(int(input().rstrip())):
    print(dp[int(input().rstrip())] % 1000000009)