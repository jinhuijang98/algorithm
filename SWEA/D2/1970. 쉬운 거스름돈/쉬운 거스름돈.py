

def change(N):
    for i in range(8):
        while N:
            if N // change_list[i] > 0:
                arr[i] = N //change_list[i]
                N = N - change_list[i]*arr[i]
                # print(N)
            break
    return arr


T = int(input())
for tc in range(1, T+1):
    N = int(input())
    # 돈의 종류만큼 arr만들기
    arr = [0] * 8
    # 돈의 종류
    # 50000
    # 10000
    # 5000
    # 1000
    # 500
    # 100
    # 50
    # 10
    change_list = [50000, 10000, 5000, 1000, 500, 100, 50, 10]
    print(f'#{tc}')
    print(*change(N))
