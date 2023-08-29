import sys
input = sys.stdin.readline

def dfs(x, adj_l):
    stack = []          # 스택 생성
    visited = [0] * n  # visited 생성
    # visited[x] = 1      # 시작점 방문 표시
    while True:
        # 현재 정점 n에 인접하고 미방문 w 찾기
        # 인덱스를 1부터 찾아서 range의 끝값을 n까지
        for w in range(n):
            # x : 시작점 / w : 다음 경로
            if adj_l[x][w] == 1 and visited[w] == 0:       # 인접해있으면서 방문하지 않았다면
                # push(v), v = w
                stack.append(x)
                x = w
                # w 방문 표시
                visited[x] = 1
                break   # for w, x에 인접인 w c 찾은 경우
        else:
            # 스택에 지나온 정점이 남아있으면
            if stack:
                # pop()해서 다시 w를 찾을 x 준비
                x = stack.pop()
            else:
                return visited






n = int(input().strip())
adj_l = [list(map(int, input().strip().split())) for _ in range(n)]
arr = [[0]*n for _ in range(n)]
for i in range(n):
    arr[i] = dfs(i, adj_l)
    print(*arr[i])