import copy

for tc in range(1, 11):
    T = int(input())
    arr = [[0]*100 for _ in range(100)]
    for i in range(100):
        arr[i] = list(map(int, input().split()))
    # arr 이차원 배열 형성
    # 출발지점 찾기
    k = []
    for i in range(100):
        if arr[0][i] == 1:
            # 출발지점의 인덱스 y에 저장
            k.append(i)
            # break
    # print(y)
    # 출발지점에서 왼/오를 먼저 보고 1이 있다면 이동
    dx = [0, 0]
    dy = [-1, 1]
    # # 시작 지점은

    # # arr[x][y]
    # 몇 번을 움직여야 하는지는 result 변수에 저장
    min_result = 10000
    # print(k)
    for j in range(len(k)):
        new_arr = copy.deepcopy(arr)
        # k[j] 열 시작점
        y = k[j]
        x = 1
        result = 1
        while x < 99:
            for i in range(2):
                if 0 <= y + dy[i] <= 99:
                    if new_arr[x][y + dy[i]] == 1:
                        new_arr[x][y] = 0
                        # x = x + dx[i]
                        y = y + dy[i]
                        # print(arr)
                        result += 1
                        break
            else:
                x += 1
                result += 1
        if new_arr[x][y] == 1:
            # print(result, k[j])
            if min_result > result:
                min_result = result
                min_index = k[j]

    print(f'#{tc} {min_index}')
    #
    # # 없다면 위로 이동
