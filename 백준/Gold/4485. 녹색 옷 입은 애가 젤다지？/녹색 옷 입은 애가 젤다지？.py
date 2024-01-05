import sys
import heapq
input = sys.stdin.readline
INF = int(1e9)


'''
[0,0]에서 시작해서 [n-1, n-1]까지
bfs로 상하좌우 움직이면서 최소값을 갱신?

'도둑루피'를 가중치로 생각하고 다익스트라 알고리즘 수행
'''

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def dijkstra():
    q = []
    heapq.heappush(q, (graph[0][0], 0, 0))
    distance[0][0] = 0

    while q:
        cost, x, y = heapq.heappop(q)

        if x == n-1 and y == n-1:
            print(f'Problem {count}: {distance[x][y]}')
            break

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if 0 <= nx < n and 0 <= ny < n:
                nc = cost + graph[nx][ny]

                if nc < distance[nx][ny]:
                    distance[nx][ny] = nc
                    heapq.heappush(q, (nc, nx, ny))



count = 1
while True:
    n = int(input().strip())
    if n == 0:
        break
    else:
        graph = [list(map(int, input().strip().split())) for _ in range(n)]
        # print(arr)
        distance = [[INF] * n for _ in range(n)]

        dijkstra()
        count += 1
        # n-1, n-1까지 최소로 이동





