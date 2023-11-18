# 12018 Yonsei TOTO

import sys
input = sys.stdin.readline
'''
이 제도는 각각의 학생들에게 마일리지를 주어 듣고 싶은 과목에 마일리지를 과목당 1~36을 분배
모두 분배가 끝이 나면 과목에 대해서 
마일리지를 많이 투자한 순으로 그 과목의 수강인원만큼 신청되는 방식
그 덕분에 다른 사람들이 신청한 마일리지를 볼 수 있게 되었다. 
성준이는 주어진 마일리지로 최대한 많은 과목을 신청하고 싶어 한다. 
(내가 마일리지를 넣고 이후에 과목을 신청하는 사람은 없다) 
마일리지는 한 과목에 1에서 36까지 넣을 수 있다.

첫째 줄에 주어진 마일리지로 최대로 들을 수 있는 과목 개수
'''
# n : 과목수
# m : 주어진 마일리지
n, m = map(int, input().strip().split())
cnt = 0
result = []
for _ in range(n):
    # p : 과목에 신청한 사람 수
    # l : 과목의 수강인원
    p, l = map(int, input().strip().split())
    # 각 사람이 마일리지를 얼마나 넣었는지.
    # 마일리지가 같다면 성준이에게 우선순위
    arr = list(map(int, input().strip().split()))
    arr.sort(reverse=True)
    if p < l:
        result.append(1)
    else:
        result.append(arr[l-1])
result.sort()
# print(result)
total = 0
for i in range(n):
    if total + result[i] <= m:
        total += result[i]
        cnt += 1
    else:
        break
print(cnt)

