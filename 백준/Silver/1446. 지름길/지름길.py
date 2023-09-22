'''
 모든 지름길은 일방통행이고, 고속도로를 역주행할 수는 없다.
세준이가 운전해야 하는 거리의 최소값
꼭 다익스트라로 풀어야 할까?
그런 생각이 드는데,,,,,,,,

'''
import heapq
import sys
# from collections import defaultdict
input = sys.stdin.readline

# n : 지름길의 개수
# d : 고속도로의 길이
n, d = map(int, input().strip().split())

# 그래프 만들기
# graph = [[] for _ in range(n)]
graph = [[] for _ in range(d+1)]
for _ in range(n):
    f, t, w = map(int, input().strip().split())
    if t <= d and t-f > w:      # 목적지를 벗어나면 안됨, 지름길이 아닐 경우 저장x
        graph[f].append([t, w])    # 단방향

# print(graph)

# 누적 거리를 계속 저장
# distance = [[] for _ in range(d+1)]
# for i in range(d+1):
#     distance[i] = i
INF = int(1e9)
distance = [INF] * (d+1)


def dijkstar(start):
    # 우선순위 큐
    pq = []
    heapq.heappush(pq, (0, start))
    distance[start] = 0

    while pq:
        # 현재 시점에서
        # 누적거리가 가장 짧은 노드에 대한 정보 꺼내기
        dist, now = heapq.heappop(pq)

        # 이미 방문한 지점 + 누적 거리가 더 짧게 방문한 적 있다면 pass
        if distance[now] < dist:
            continue

        # now의 graph가 존재한다면
        if graph[now]:
            for next in graph[now]:

                next_node = next[0]
                cost = next[1]

                # next_node로 가기 위한 누적 거리
                new_cost = dist + cost

                # 누적 거리가 기존보다 크네? => 지름길 끼리도 비교해야 하므로 필요
                if distance[next_node] <= new_cost:
                    continue
                # 여기서의 next_node와 new_cost와 아래에서의 ~~가 다르기 때문에 여기서도
                # 값을 비교해서 push해주고 아래에서도 해줘야 함
                distance[next_node] = new_cost
                heapq.heappush(pq, (new_cost, next_node))


        # now의 graph가 존재하지 않는다면 그냥 한 칸씩 이동
        next_node = now + 1
        new_cost = dist + 1

        if next_node < d+1:
            # 누적 거리가 기존보다 크네?
            if distance[next_node] <= new_cost:
                continue

            distance[next_node] = new_cost
            heapq.heappush(pq, (new_cost, next_node))


start = 0
dijkstar(start)
print(distance[d])