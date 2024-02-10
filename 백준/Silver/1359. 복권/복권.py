from itertools import combinations

n, m, k = map(int,input().split())

ans = 0
all = [*combinations([i for i in range(n)], m)]  # 모든 경우의 수

for i in all:
  cnt = 0
  for j in range(m):
      if i[j] < m:  # 0 ~ m-1이 복권에 당첨되는 번호라고 가정한다.
        cnt += 1
  if cnt >= k:  # k 개 이상 맞은 경우
    ans += 1

print(ans / len(all))