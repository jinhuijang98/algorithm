from collections import deque

N = int(input())
arr = deque()
for i in range(1, N+1):
    arr.append(i)
# print(arr)

for i in range(N-1):
    arr.popleft()
    arr.append(arr.popleft())
print(arr[0])