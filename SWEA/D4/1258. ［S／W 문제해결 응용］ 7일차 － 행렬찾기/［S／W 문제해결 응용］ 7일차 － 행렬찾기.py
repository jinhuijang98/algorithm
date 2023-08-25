

'''
1. 2차원 배열로 받아서
2. 행 우선순회 하면서 숫자를 발견하면
3. dfs로 해당 부분의 오른쪽 끝값을 찾아준다. (오른쪽으로 쭉, 아래로 쭉)
4. 해당 행렬의 행, 열 값을 따로 저장해주고
4. 행렬의 모든 값을 0으로 바꿈

탐색 끝날 때까지
'''

def find_size(r, c):
    global cnt
    cnt += 1
    l1_r = r
    l2_c = c
    while True:
        if c + 1 < N:
            if arr[r][c + 1] != 0:
                c += 1
            else:
                break
        else:
            break

    while True:
        if r + 1 < N:
            if arr[r + 1][c] != 0:
                r += 1
            else:
                break
        else:
            break
    r1_r = r
    r2_c = c

    # 5. 행렬의 모든 값을 0으로 바꿔버린다.
    for r in range(l1_r, r1_r + 1):
        for c in range(l2_c, r2_c + 1):
            arr[r][c] = 0

    size_multiple = (r1_r - l1_r + 1) * (r2_c - l2_c + 1)
    size = [r1_r - l1_r + 1, r2_c - l2_c + 1, size_multiple]
    return size

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    # 다음 n줄에 nxn 행렬 => arr
    # 1. 2차원 배열로 받아서
    arr = [list(map(int, input().split())) for _ in range(N)]
    size_list = []
    cnt = 0

    # 2. 행 우선순회 하면서 숫자를 발견하면
    for r in range(N):
        for c in range(N):
            # 3. dfs로 해당 부분의 오른쪽 끝값을 찾아준다. (오른쪽 쭉, 아래 쭉)
            if arr[r][c] != 0:
                size_list.append(find_size(r, c))

    size_list.sort(key=lambda x:x[2])

    for i in range(len(size_list) -1):
        if size_list[i][2] == size_list[i+1][2]:
            if size_list[i][0] < size_list[i+1][0]:
                pass
            else:
                size_list[i], size_list[i+1] = size_list[i+1], size_list[i]

    result = ''
    for j in size_list:
        result += str(j[0]) + ' ' + str(j[1]) + ' '

    print(f'#{tc} {cnt} {result}')