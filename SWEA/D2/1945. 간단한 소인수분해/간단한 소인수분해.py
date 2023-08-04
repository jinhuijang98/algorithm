T = int(input())

for tc in range(1, T+1):
    N = int(input())
    # a, b, c, d, e의 초기값 설정
    a = 0
    b = 0
    c = 0
    d = 0
    e = 0
    while N > 1:
        if N % 2 == 0:
            a += 1
            N = N / 2
        if N % 3 == 0:
            b += 1
            N = N /3
        if N % 5 == 0:
            c += 1
            N = N/5
        if N % 7 == 0:
            d += 1
            N = N/7
        if N % 11 == 0:
            e += 1
            N = N/11
    print(f'#{tc} {a} {b} {c} {d} {e}')