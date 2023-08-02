# N, M 입력 받기
N, M = map(int, input().split())

# N번 만큼 붕어빵 모양 입력받기
for i in range(N):
    shape = input()


    # M개 순회하면서 빈 문자열에 거꾸로 입력
    re_shape = ''
    for j in shape:
        re_shape = j + re_shape

    print(re_shape)