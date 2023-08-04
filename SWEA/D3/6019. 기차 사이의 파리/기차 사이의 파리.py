
T = int(input())

for tc in range(1, T+1):
    D, A, B, F = map(int, input().split())
    # D = A*h + B*h
    h = D / (A+B)
    print(f'#{tc} {h*F}')
