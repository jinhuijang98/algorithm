T = int(input())

for tc in range(1, T+1):
    n = int(input())
    text = input()
    cnt = 0
    max_v = 0
    for i in range(n):
        if text[i] == '1':
            cnt += 1
            if max_v < cnt:
                max_v = cnt
        else:
            cnt = 0

    print(f'#{tc} {max_v}')