from collections import deque
import sys
input = sys.stdin.readline
# 좌표 (0,0)부터 시작해서 정육각형 범위로 탐색을 하면서 회색 건물을 만나면 카운트
# 1을 탐색하는 것이 아닌 0을 탐색.
col, row = map(int, input().strip().split())
# w : 가로, h : 높이
# +2씩 해줌. 외벽과 닿는 면을 모두 0으로 처리해줌
graph = [[0] * (col+2) for _ in range(row+2)]
# print(graph)
for i in range(1, row+1):
    graph[i][1:col+1] = map(int, input().split())

# 이동할 수 있는 범위 설정
dy = [0, 1, 1, 0, -1, -1]
# dy는 홀수인지 짝수인지에 따라 달라짐
# 홀수인 경우
dx = [[1, 0, -1, -1, -1, 0],[1, 1, 0, -1, 0, 1]]

# y가 행, x가 열
def bfs(y, x):
    q = deque()
    q.append((y, x))
    # 방문 체크 배열 생성
    visited = [[False]*(col+2) for _ in range(row+2)]
    visited[y][x] = True
    cnt = 0
    while q:
        y, x = q.popleft()

        for i in range(6):
            ny = y + dy[i]
            nx = x + dx[y%2][i]
            if 0 <= ny < row + 2 and 0 <= nx < col+2:
                if graph[ny][nx] == 0 and not visited[ny][nx]:
                    q.append((ny, nx))
                    visited[ny][nx] = True
                # 근데 이게 어케 둘레가 되는거지..?
                elif graph[ny][nx] == 1:
                    cnt += 1
    return cnt

print(bfs(0,0))