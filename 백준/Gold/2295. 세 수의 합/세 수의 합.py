# 2295 세 수의 합

import sys
input = sys.stdin.readline

n = int(input().strip())
# x + y = k -z
arr = [int(input().strip()) for _ in range(n)]
arr_sum = []
for i in range(n):
    for j in range(i, n):
        arr_sum.append(arr[i] + arr[j])

arr_sum.sort()
result = 0
for i in range(n):
    for j in range(i, n):
        # a = k - z
        a = arr[j] - arr[i]
        start = 0
        end = len(arr_sum) - 1
        while start <= end:
            mid = (start + end) // 2
            b = arr_sum[mid]
            if a > b:
                start = mid + 1
            elif a < b:
                end = mid - 1
            else:
                result = max(result, arr[j])
                break
print(result)