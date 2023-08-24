import sys
input = sys.stdin.readline

N = int(input())
arr = [[0]*100 for _ in range(100)]
cnt = 0
for i in range(N):
    x, y = map(int, input().split())
    for j in range(x, x+10):
        for k in range(y, y+10):
            arr[j][k] += 1

for j in range(100):
    for k in range(100):
        if arr[j][k] >= 1:
            cnt += 1
print(cnt)