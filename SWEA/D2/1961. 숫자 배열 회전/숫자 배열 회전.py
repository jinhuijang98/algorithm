
T = int(input())

for tc in range(1, T+1):
    # N x N
    N = int(input())
    # str처럼 붙이기 위해 type str로 가져옴
    arr = [list(input().split()) for _ in range(N)]
    # 90도 회전은 행 뒤부터 / 열은 순서대로
    # 결과물의 1열 완성
    print(f'#{tc}')
    new_arr1 = []
    for j in range(N):
        string = ''
        for i in range(N-1, -1, -1):
            string += arr[i][j]
        new_arr1.append(string)
        # print(new_arr1)

    # 180도 회전은 행 뒤 부터 / 열도 뒤부터
    # 결과물의 2열 완성
    new_arr2 = []
    for i in range(N-1, -1, -1):
        string = ''
        for j in range(N-1, -1, -1):
            string += arr[i][j]
        new_arr2.append(string)
        # print(new_arr2)

    # 270도 회전은 행은 처음부터 / 열은 뒤부터
    # 결과물의 3열 완성
    new_arr3 = []
    for j in range(N-1, -1, -1):
        string = ''
        for i in range(N):
            string += arr[i][j]
        new_arr3.append(string)
        # print(new_arr3)

    result = []
    result.append(new_arr1)
    result.append(new_arr2)
    result.append(new_arr3)
    # 최종 결과물 출력
    for j in range(N):
        for i in range(3):
            print(result[i][j], end=' ')
        print()