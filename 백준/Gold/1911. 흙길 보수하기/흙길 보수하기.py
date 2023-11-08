# 1911 흙길 보수하기

import sys

input = sys.stdin.readline

n, l = map(int, input().strip().split())
puddle = [list(map(int, input().strip().split())) for _ in range(n)]
puddle.sort()

# 웅덩이를 덮은 마지막 널빤지의 위치
cur = 0
# 널빤지의 개수
cnt = 0
for i in puddle:
    # 시작 지점 i[0]
    # 끝 지점 i[1]
    if i[0] > i[1]:
        continue

    # 이전 웅덩이에서 덮은 널빤지가 해당 웅덩이를 덮고 있는 경우
    if cur > i[0]:
        i[0] = cur

    # 널빤지의 개수 count
    if i[0] < i[1]:
        x = i[1] - i[0]
        if x % l == 0:
            cnt += x // l
            i[0] = i[0] + x
        else:
            cnt += x // l + 1
            i[0] = i[0] + (x // l + 1)*l

    cur = i[0]

print(cnt)
