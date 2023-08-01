T = int(input())

for tc in range(T):
    N, M = map(int, input().split())
    count_v = 0
    # N부터 M까지의 값 탐색
    for i in range(N, M+1):
        # 0을 포함하고 있다.. -> str로 바꾸는 것밖에 없는 것 같은데
        for j in str(i):
            if j == '0':
                count_v += 1
    print(count_v)
