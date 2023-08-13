T = int(input())
for tc in range(1, T+1):
    # 초기 배열 형성
    arr = [[0]*15 for _ in range(5)]
    for i in range(5):
        arr[i] = list(input())
    x =''
    for i in range(15):
        for j in range(5):
            try:
                x += arr[j][i]
            except:
                pass
    print(f'#{tc} {x}')