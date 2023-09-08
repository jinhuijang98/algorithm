import sys
input = sys.stdin.readline

n = int(input().strip())

arr = list(map(int, input().strip().split()))

arr2 = arr.copy()
budget = int(input().strip())

if sum(arr) <= budget:
    print(max(arr))
else:
    # 예산의 평균을 우선 기준으로 잡음
    flag = budget // n
    while sum(arr) >= budget:
        for i in range(n):
            if arr2[i] > flag:
                arr2[i] = flag
        if sum(arr2) > budget:
            break
        arr2 = arr.copy()
        flag += 1
    print(flag-1)
