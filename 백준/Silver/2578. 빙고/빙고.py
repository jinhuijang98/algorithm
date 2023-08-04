# 철수 빙고판
arr = [[0]*5 for _ in range(5)]

# 정답빙고판
bingo = [[0]*5 for _ in range(5)]

for i in range(5):
    arr[i] = list(map(int, input().split()))

for i in range(5):
    bingo[i] = list(map(int, input().split()))
# bingo = list(input().split() for _ in range(25))
# print(bingo)
#
# for i in range(5):
#     for j in range(5):
#         if arr[i][j] == bingo[i]
# 빙고 판정하는 함수(행, 열, 대각선)
def bingo_find_r(ar):
    # 행 빙고 판정하는 함수
    rlt = 0
    for i in range(5):
        all_zero = 0
        for j in range(5):
            if ar[i][j] == 0:
                all_zero += 1
        if all_zero == 5:
            rlt += 1
    return rlt

def bingo_find_c(ar):
    # 열 빙고 판정하는 함수
    rlt = 0
    for i in range(5):
        all_zero = 0
        for j in range(5):
            if ar[j][i] == 0:
                all_zero += 1
        if all_zero == 5:
            rlt += 1
    return rlt


def bingo_find_cr(ar):
    # 대각선 빙고 판정하는 함수
    # 대각선 빙고의 경우 for문 밖에 all_zero를 넣어야 초기화가 안됨!!!
    rlt = 0
    all_zero = 0
    for i in range(5):
        # for j in range(5):
        if ar[i][i] == 0:
            all_zero += 1
        if all_zero == 5:
            rlt += 1
    return rlt

def bingo_find_cr2(ar):
    # 대각선 빙고 판정하는 함수
    # 대각선 빙고의 경우 for문밖에 all_zero를 넣어야 초기화가 안됨
    rlt = 0
    all_zero = 0
    for i in range(5):
        # for j in range(5):
        if ar[i][4-i] == 0:
            all_zero += 1
        if all_zero == 5:
            rlt += 1
    return rlt



result = 0
rll = 0
for i in range(5):
    for j in range(5):
        # bingo[i][j]

        check = 0

        # while check:
        for k in range(5):
            for l in range(5):
                if bingo[i][j] == arr[k][l]:
                    arr[k][l] = 0
                    result += 1
                    check = 1
            if check == 1:
                break
            # check
        if result >= 12:
            rll = bingo_find_r(arr) + bingo_find_c(arr) + bingo_find_cr(arr) + bingo_find_cr2(arr)
            # print(f'{result}: {rll} {bingo_find_r(arr)} {bingo_find_c(arr)} {bingo_find_cr(arr)} {bingo_find_cr2(arr)}')
            if rll >= 3:
                # print(result)
                break

    if rll >= 3:
        break

print(result)

        # for k in range(5):
        #     for l in range(5):
        #         if bingo[i][j] == arr[k][l]:
        #             arr[k][l] == 0
        #             result += 1
        #             continue
        #             # for a in range(5):
        #             #     if arr[k][a] == 0
        #         if result>=5 and (bingo_find_r(arr) + bingo_find_c(arr) + bingo_find_cr(arr) + bingo_find_cr2(arr)) >= 3:
        #             print(result)