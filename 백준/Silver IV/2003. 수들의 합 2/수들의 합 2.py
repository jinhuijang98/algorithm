# 2003 수들의 합 2

import sys
input = sys.stdin.readline

n, m = map(int, input().strip().split())

arr = list(map(int, input().strip().split()))

'''
i, i+1, ..., j까지의 합이 m이 되는 경우의 수

'''

start = 0
end = 0
cnt = 0
while end < n:
    total = 0
    for i in range(start, end+1):
        total += arr[i]
    if total == m:
       cnt += 1
       end += 1
       start += 1
    elif total > m:
        start +=1
    else:
        end +=1
print(cnt)