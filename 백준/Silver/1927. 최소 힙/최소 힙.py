'''
배열에 자연수 x를 넣는다.
배열에서 가장 작은 값을 출력하고, 그 값을 배열에서 제거한다.
다음 N개의 줄에는 연산에 대한 정보를 나타내는 정수 x가 주어짐
만약 x가 자연수라면 배열에 x라는 값을 넣는(추가하는) 연산이고,
x가 0이라면 배열에서 가장 작은 값을 출력하고 그 값을 배열에서 제거하는 경우
'''

# heapq 이용해 시간초과 해결
import sys
import heapq

input = sys.stdin.readline
# 연산의 개수
n = int(input().strip())

hq = []
for _ in range(n):
    x = int(input().strip())
    # d.sort()
    if x == 0 :
        if hq:
            print(hq[0])
            heapq.heappop(hq)
        else:
            print(0)
    else:
        heapq.heappush(hq, x)