T = int(input())
#
# for tc in range(1, T+1):
#     A, B = map(str, input().split())
#
#     kmp(A, B)

for tc in range(1, T+1):
    A, B = map(str, input().split())
    # 몇 번 겹치는 지 탐색
    cnt = 0
    # A의 길이만큼 새로운 리스트를 만들어서 만약 겹친다면 1의 값을 넣고
    # 1의 값이 존재한다면(값이 0이 아니라면) 탐색을 건너 뜀
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