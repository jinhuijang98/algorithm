n = int(input())

arr = list(map(int, input().split()))

budget = int(input())

if sum(arr) <= budget:
    print(max(arr))
else:
    start = 0
    end = sum(arr)
    while start <= end:
        s = 0
        mid = (start+end)//2
        if mid == start:
            break
        for i in arr:
            if i <= mid:
                s += i
            else:
                s += mid
        if s > budget:
            end = mid
        else:
            start = mid
    print(mid)
