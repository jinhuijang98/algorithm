
T = int(input())
for tc in range(1, T+1):
    # n :과목 수
    # k : k개의 과목을 선택하여 넣음
    n, k = map(int, input().split())
    # k개로 만들 수 있는 최대 총점
    arr = list(map(int, input().split()))
    arr.sort(reverse=True)
    total = 0
    for i in range(n):
        s = 0
        for j in range(k):
            if i+j < len(arr):
                s += arr[i+j]
        if total < s:
            total = s
    print(f'#{tc} {total}')