

def bfs(s):      # s : 시작점
    q = []          # q 만들고 시작
    q.append(s)     # 시작점 q에 넣기
    visited[s] = 1      # 거리 구해야 하니까 시작점 방문 =1
    while q:
        n = q.pop(0)    # 시작 위치
        for w in range(101):
            if visited[w] == 0 and adj_l[n][w] == 1:    # 아직 방문하지 않았으면서 인접해있다면
                q.append(w)     # w를 q에 넣고
                visited[w] = visited[n] + 1   # visited를 이전 값에서 +1로 바꾸기
    return visited





for tc in range(1, 11):
    # L : 입력 받는 데이터의 길이
    # S : 시작점
    L, S = map(int, input().split())
    # from, to 쌍 받는 arr
    arr = list(map(int, input().split()))
    # 방문 리스트 형성
    visited = [0]*101 # 1~101
    # 인접 리스트 형성
    # 번호 1 ~ 100
    adj_l = [[0]*101 for _ in range(101)]
    # print(adj_l)
    for i in range(L//2):
        v1, v2 = arr[i*2], arr[i*2 + 1]
        adj_l[v1][v2] = 1       # 단방향이므로 여기까지만
    bfs(S)
    result = 0          # 최종 가장 큰 visited 값
    # for i in range(101):
    #     if visited[i] > result:
    #         result = visited[i]
    # # 그 값과 일치하는 인덱스 값 가져옴
    # for i in range(101):
    #     if visited[i] == result:
    #         x = i

    for i, rlt in enumerate(visited):   # i = 인덱스, rlt = 값
        if result <= rlt:   # 만약 값이 result 보다 크거나 같다면(같은 경우 인덱스 큰 값 출력이므로)
            result = rlt    # result를 rlt로 가져오고
            x = i   # 인덱스를 i에 저장
    print(f'#{tc} {x}')

