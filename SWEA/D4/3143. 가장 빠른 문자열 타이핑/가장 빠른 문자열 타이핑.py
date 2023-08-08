T = int(input())
#
# for tc in range(1, T+1):
#     A, B = map(str, input().split())
#
#     kmp(A, B)

for tc in range(1, T+1):
    A, B = map(str, input().split())
    cnt = 0
    new_list = [0] *len(A)
    for i in range(len(A)-len(B)+1):
        if new_list[i] == 0:
            new_str = ''

            for j in range(len(B)):
                new_str += A[i+j]
            if new_str == B:
                for k in range(len(B)):
                    new_list[i+k] = 1
                cnt += 1
            # break
    result = len(A) - len(B) * cnt + cnt
    print(f'#{tc} {result}')