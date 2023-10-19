# 못품

import sys
input = sys.stdin.readline
d, n, m = map(int, input().split())
stone = [int(input()) for _ in range(n)]
stone.sort()
start = 0
end = d
dist = 0
while start <= end:
    mid = (start + end) // 2
    count = 0 # 돌의 개수
    now = 0
    min_distance = d
    for x in stone:
        if x - now >= mid:
            min_distance = min(min_distance, x - now)
            now = x
        else:
            count += 1

    min_distance = min(min_distance, d - now)

    if count > m:
        end = mid - 1
    else:
        dist = max(dist, min_distance)
        start = mid + 1

print(dist)