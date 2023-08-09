T = 10

for tc in range(1, T+1):
    N = input()
    A = input()
    B = input()

    b_cnt = 0
    for i in B:
        # B의 글자수 세기
        b_cnt += 1

    a_cnt = 0
    for i in A:
        a_cnt += 1

    result = 0
    for i in range(b_cnt-a_cnt+1):
        new_str = ''
        for j in range(a_cnt):
            new_str += B[i+j]
        if A == new_str:
            result += 1
    print(f'#{tc} {result}')
