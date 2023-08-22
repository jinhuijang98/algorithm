import sys
input = sys.stdin.readline


# 모든 국가를 여행하기 위해 타야 하는 비행기 종류의 최소 개수
def dfs(x):         # x : 시작점
    stack = []
    visited = [0] * (N+1)
    visited[x] = 1          # 시작점 1로 바꾸고
    # stack.append(x)
    cnt = 0
    while True:
        for w in adj[x]:
            if visited[w] == 0:     # 아직 방문하지 않았다면
                cnt += 1
                stack.append(x)     # i를 append하고
                x = w
                visited[x] = 1      # 값을 1로 바꿔줌
                break
        else:
            if stack:
                x = stack.pop()
            else:
                break
    return cnt




T = int(input())
for tc in range(T):
    # N : 국가의 수
    # M : 비행기의 종류
    N, M = map(int, input().strip().split())
    # arr = [list(map(int, input().strip().split())) for _ in range(N+1)]
    adj = [[] for _ in range(N+1)]
    for i in range(M):
        v1, v2 = map(int, input().strip().split())
        adj[v1].append(v2)
        adj[v2].append(v1)      # 왕복
    # print(adj)
    print(dfs(1))
