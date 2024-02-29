# 16938 캠프 준비

'''
알고리즘 캠프
문제
백준이를 도와 알고리즘 캠프에 사용할 문제를 고르려고 함
백준이는 문제를 N개 가지고 있고, 모든 문제의 난이도를 정수로 수치화함
i번째 문제의 난이도는 A_j
캠프에 사용할 문제는 두 문제 이상이어야 함. 문제가 너무 어려우면 학생들이 멘붕에 빠지고,
문제가 너무 쉬우면 학생들이 실망
문제 난이도의 합은 L<= <= R
가장 어려운 문제와 가장 쉬운 난이도 차이는 x보다 크거나 같아야 함
캠프에 사용할 문제를 고르는 방법의 수

'''

import sys
input = sys.stdin.readline

n, l, r, x = map(int, input().strip().split())

arr = list(map(int, input().strip().split()))

arr.sort()

ans = 0

def dfs(depth, idx, maxim, mini, diff):
    global ans
    # 난이도의 합이 r보다 크면 return
    if diff > r:
        return
    # 선택한 문제가 2개 이상 & 난이도가 l과 r사이라면
    elif depth >= 2 and l <= diff <= r:
        # 가장 어려운 문제와 가장 쉬운 난이도의 차이가 x보다 크거나 같다면
        if not(maxim == None or mini == None) and maxim - mini >= x:
            ans += 1

    for i in range(idx, len(arr)):
        if mini == None:
            dfs(depth+1, i+1, arr[i], arr[i], diff+arr[i])
        else:
            dfs(depth+1, i+1, arr[i], mini, diff+arr[i])



dfs(0, 0, None, None, 0)
print(ans)