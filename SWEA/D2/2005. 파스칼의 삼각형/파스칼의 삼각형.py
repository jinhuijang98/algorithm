

T = int(input())


# pascal 함수 정의
def pascal(arr, i, j):
    # i >= 2 & j >= 1 여야 연산 수행
    if i >= 2 and j >= 1 and i > j:
        # 재귀 이용해서 진행
        arr[i][j] = pascal(arr, i-1, j-1) + pascal(arr, i-1, j)
    # 이 조건문이 들어가지 않으면 값을 다시 0 -> 1로 바꾸는 오류가 생김
    # if 문에 작성했다 하더라도 재귀 함수 내에서 오류 발생
    # elif j > i:
    #     arr[i][j] = 0
    # 만약 그렇지 않은 경우에는 모두 1로
    else:
        return 1
    return arr[i][j]


for tc in range(1, T+1):
    # 값을 받는 N
    N = int(input())
    # 처음 0으로 모든 값 초기화한 2차원 배열(N*N) 만듦
    arr = [[0]*N for _ in range(N)]
    for i in range(N):
        for j in range(N):
            # 만약 j < i 인 경우에만 함수 이용해서 구함
            if j < i:
                arr[i][j] = pascal(arr, i, j)
            # arr[i][i] = 1의 값으로
            elif j ==i :
                arr[i][j] = 1
            # j > i 인 경우 0으로 값 채워줌
            else:
                arr[i][j] = 0
    print(f'#{tc}')
    # arr을 돌면서 0이 아닌 값만 출력
    for i in range(N):
        for j in range(N):
            if arr[i][j] != 0:
                print(arr[i][j], end=" ")
        print()



