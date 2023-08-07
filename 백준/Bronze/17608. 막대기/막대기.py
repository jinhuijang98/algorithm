import sys
input = sys.stdin.readline

N = int(input())

arr = []
for i in range(N):
    arr.append(int(input()))

max_v = arr[-1]
count_v = 1
for i in range(N-1, -1, -1):
    if max_v < arr[i]:
        max_v = arr[i]
        count_v += 1

print(count_v)