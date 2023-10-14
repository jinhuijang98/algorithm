# 18870 좌표 압축

import sys
input = sys.stdin.readline

M = int(input().strip())


# 행성의 크기가 한 줄에 하나씩 1번 우주부터 차례대로 주어짐
arr = list(map(int, input().strip().split()))
arr2 = sorted(list(set(arr)))
dic = {arr2[i] : i for i in range(len(arr2))}
# print(dic)
for i in arr:
    print(dic[i], end= ' ')