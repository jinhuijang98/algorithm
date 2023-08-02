T = 10

for tc in range(1, T+1):
    N = int(input())
    arr = list(map(int, input().split()))
    count_v = [0] * N

    for i in range(2, N-1):
        # i를 기준으로 양옆 2개씩 값이 크다면
        while arr[i] > arr[i-2] and arr[i] > arr[i-1] and arr[i] > arr[i+1] and arr[i] > arr[i+2]:
            count_v[i] += 1
            arr[i] = arr[i]-1
    result = 0
    for rlt in count_v:
        result += rlt
    print(f'#{tc} {result}')
