'''
5
8
1 2 2
1 3 3
1 4 1
1 5 10
2 4 2
3 4 1
3 5 1
4 5 3
1 5
'''
import sys
input = sys.stdin.readline
# 도시의 개수
n = int(input().strip())
# 버스의 개수
m = int(input().strip())

graph = [[] for _ in range(n+1)]
for _ in range(m):
    f, t, w = map(int, input().strip().split())
    graph[f].append([t, w])
# print(graph)

start, end = map(int, input().strip().split())

INF = int(1e9)
distance = [INF] * (n+1)
import heapq
def dijkstar(start):
    pq = []
    heapq.heappush(pq, (0, start))
    distance[start] = 0

    while pq:
        dist, now = heapq.heappop(pq)

        if distance[now] < dist:
            continue

        for next in graph[now]:
            next_node = next[0]
            cost = next[1]

            new_cost = dist+cost

            if distance[next_node] <= new_cost:
                continue

            distance[next_node] = new_cost
            heapq.heappush(pq, (new_cost, next_node))


dijkstar(start)
print(distance[end])