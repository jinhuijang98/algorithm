# 흩날리는 시험지 속에서 내 평점이 느껴진거야
N, K = map(int, input().split())
arr = list(map(int, input().split()))

answer = 0
left, right = 0, int(1e5)*20+1
while left <= right:
    mid = (left+right)//2
    # 그룹 나누기
    group = 0
    score = 0
    for s in arr:
        score += s
        if score >= mid:
            group += 1
            score = 0
    # 다음
    if group >= K:
        answer = mid
        left = mid+1
    else:
        right = mid-1

print(answer)