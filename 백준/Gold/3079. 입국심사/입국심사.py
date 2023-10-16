# 3079 입국심사

import sys
input = sys.stdin.readline

n, m = map(int, input().strip().split())

T = [int(input().strip()) for _ in range(n)]

T.sort()

'''

'''
start = T[0]
end = max(T) * m
ans = end
while start <= end:
    result = 0
    mid = (start + end) // 2

    for i in T:
        result += (mid//i)

    if result >= m:
        end = mid - 1
        ans = min(mid, ans)
    else:
        start = mid + 1


print(ans)