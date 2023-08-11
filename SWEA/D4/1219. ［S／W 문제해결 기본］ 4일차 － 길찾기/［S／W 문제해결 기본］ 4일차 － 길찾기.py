# n : 시작점, V: 끝 점? adj_m : 인접행렬
def dfs(n, V, adj_m):
    stack = []
    # 0 ~ 99까지 100개로 만들어야 함
    visited = [0] * (V+1)
    visited[n] = 1
    while True:
        # range가 0부터 100 -> 0부터 99까지
        for w in range(0, V+1):
            # 인접했고 방문하지 않았다면
            if adj_m[n][w] == 1 and visited[w] == 0:
                # stack에 추가
                stack.append(n)
                # 시작점 w로 변경
                n = w
                # 방문 값 1로
                visited[n] = 1
                break
        else:
            if stack:
                n = stack.pop()
            else:
                if visited[n] == 1 and visited[V] == 1:
                    return 1
                else:
                    return 0


for _ in range(1, 11):
    tc, E = map(int, input().split())
    V = 99
    # 인접 행렬
    adj_m = [[0] * (V+1) for _ in range(V+1)]
    # 정보를 나타내는 값
    arr = list(map(int, input().split()))
    for i in range(E):
        # v1 : 시작점, v2 : 끝점
        v1, v2 = arr[i * 2], arr[i * 2 + 1]
        adj_m[v1][v2] = 1
    print(f'#{tc} {dfs(0, 99, adj_m)}')

