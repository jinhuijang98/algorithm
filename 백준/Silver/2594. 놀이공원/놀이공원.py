# 2594 놀이공원

'''
놀이공원에서 일하는 모든 사람들은
어떤 놀이기구가 작동을 시작하기 10분 전부터,
모든 놀이기구가 작동을 멈춘 후 10분 후까지는 쉴 수 없고,
그 나머지 일과 시간에만 쉴 수 있다.
하루 일과를 시작하는 시각은 오전 10시이고, 일과를 마치는 시각은 오후 10시이다.
'''

import sys
input = sys.stdin.readline
# from datetime import datetime

N = int(input().strip())

hour = []
for _ in range(N):
    s, e = input().strip().split()
    s = int(s[:2]) * 60 + int(s[2:])
    e = int(e[:2]) * 60 + int(e[2:])
    hour.append([s-10 , e+10])
hour.sort()
hour.insert(0, [600, 600])
hour.append([1320, 1320])

max_time = 0
for i in range(1, N+2):

    x = hour[i][0] - hour[i-1][1]
    if x >= 0:
        max_time = max(max_time, x)
    else:
        hour[i][0] = hour[i-1][1]
    if hour[i][1] < hour[i][0]:
        hour[i][1] = hour[i][0]
print(max_time)