import sys
input = sys.stdin.readline

# 기둥의 개수
N = int(input().strip())

arr = []
# L : 기둥의 왼쪽 면의 위치
# H : 높이
for i in range(N):
    L, H = map(int, input().strip().split())
    arr.append([L, H])
# arr = [[0] * 2 for _ in range(L)]
# print(arr)
# L 기준으로 정렬 (왼쪽 면의 위치)
arr.sort()
# print(arr)
max_h = 0
for i in range(N):
    if max_h <= arr[i][1]:
        max_h = arr[i][1]
        x = i
# print(max_h, x)    # 최대 높이와 그걸 나타내는 인덱스

# 창고의 초기값
rlt = 0
# print(rlt)

for i in range(x):
    # 비교할 값이 그 다음 값이랑만 비교하면 됨
    if i < x:
        if arr[i][1] < arr[i+1][1]:
            rlt += (arr[i+1][0] - arr[i][0]) * arr[i][1]
        else:
            arr[i+1][1] = arr[i][1]
            rlt += (arr[i + 1][0] - arr[i][0]) * arr[i][1]

rlt += max_h
# print(rlt)
for i in range(N-1, x, -1):
    if i > x:
        if arr[i][1] < arr[i-1][1]:
            rlt += (arr[i][0] - arr[i-1][0]) * arr[i][1]
        else:
            arr[i-1][1] = arr[i][1]
            rlt += (arr[i][0] - arr[i-1][0]) * arr[i][1]
print(rlt)
