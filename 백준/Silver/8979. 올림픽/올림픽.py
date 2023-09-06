import sys
input = sys.stdin.readline

# n : 국가의 수
# k : 등수를 알고 싶은 국가
n, k = map(int, input().strip().split())

# 국가를 나타내는 정수, 금, 은, 동메달의 수
arr = [list(map(int, input().strip().split())) for _ in range(n)]
# print(arr)

first = []
second = []
third = []
# 동 -> 은 -> 금 순서대로 정렬해야 함
arr.sort(key = lambda x:x[3], reverse=True)
arr.sort(key = lambda x:x[2], reverse=True)
arr.sort(key=lambda x:x[1], reverse=True)
# print(arr)

# 정렬한 후, 공동 순위일 수 있으므로
# 그것 확인 => 좌, 우로만 확인하면 됨
for i in range(n):
    if arr[i][0] == k:
        x = arr.index(arr[i])
        break
# print(x)

# 만약 k가 0이라면 그대로 1출력
if x == 0:
    print(1)
else:
    for i in range(x):
        if arr[i][1] == arr[x][1] and arr[i][2]==arr[x][2] and arr[i][3] == arr[x][3]:
            x = i
            break
    print(x + 1)
# k값에서 -1한 인덱스를 기준
# x = arr.pop(k-1)
