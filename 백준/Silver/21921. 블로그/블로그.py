import sys

input = sys.stdin.readline

# n, x
n, x = map(int, input().strip().split())

# 1일차 ~ n일차까지 하루 방문자 수
arr = list(map(int, input().strip().split()))
# max_v = 0
max_v = sum(arr[0:x])
k = sum(arr[0:x])
for i in range(n-x):
    k = k - arr[i]
    k = k + arr[i+x]
    if max_v < k:
        max_v = k

cnt = 0
k = sum(arr[0:x])
if k == max_v:
    cnt += 1
for i in range(n-x):
    k = k - arr[i]
    k = k + arr[i+x]
    if max_v == k:
        cnt += 1
if max_v == 0:
    print('SAD')
else:
    print(max_v)
    print(cnt)






# print('진희야 안녕')