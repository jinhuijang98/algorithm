# 16967 배열 복원하기

import sys

input = sys.stdin.readline

h, w, x, y = map(int, input().strip().split())

arr = [list(map(int, input().strip().split())) for _ in range(h+x)]


arr2 = arr.copy()
'''

'''

# for i in range(x):
#     for j in range(y):
#         arr2[h+i][w+j] = arr[h+i][w+j] - arr[i][j]

A = [[0] * w for _ in range(h)]

for i in range(h):
    for j in range(w):
        A[i][j] = arr2[i][j]

for i in range(h):
    for j in range(w):
        if i+x < h and j+y < w:
            A[i+x][j+y] -= A[i][j]
for i in range(h):
    print(*A[i])
# aa = []
# check = True
# for i in range(h+x):
#     for j in range(w+y):
#         if arr[i][j] == 0:
#             check = False
#             break
#     else:
#         aa.append(arr[i])
#
# for i in range(len(aa)):
#
