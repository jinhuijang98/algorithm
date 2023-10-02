
import sys
input = sys.stdin.readline

n, k, b = map(int,input().split())
trafficLight = [i for i in range(1,n+1)]

for i in range(b):
    trafficLight[int(input())-1] = -1

res = 0
for i in range(k):
    if trafficLight[i] == -1:
        res += 1

count = res
for i in range(1,n-k+1):
    if trafficLight[i-1] == -1:
        count -=1
    if trafficLight[i+k-1] == -1:
        count += 1

    res = min(res, count)

print(res)