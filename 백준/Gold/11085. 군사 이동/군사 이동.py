# 모르겠다..
# 11085 군사 이동

import sys
import heapq
input = sys.stdin.readline


# p개의 지점 w개의 길
p, w = map(int, input().strip().split())
# 0부터 p-1까지
# visited = [[0] * p for _ in range(p)]
# print(visited)

# 처음에 bfs를 생각했는데 트리 + Union으로도 풀 수 있구나


# c : 백준 월드 수도
# v : 큐브 월드 수도
c, v = map(int, input().strip().split())

# p개만큼의 부모를 만들기, 초기에는 각 노드가 자기 자신을 부모로 가리키도록
parent = list(range(p))

# 재귀적으로 부모 찾기
def find_parent(parent, x):
    if parent[x] != x:
        return find_parent(parent, parent[x])
    return x


# 두 노드를 합치는 함수, 각 노드의 부모를 찾아서 연결
def union_parent(parent, a, b):
    a = find_parent(parent, a)
    b = find_parent(parent, b)
    if a < b:
        parent[b] = a
    else:
        parent[a] = b

# 간선 정보 저장. 힙을 사용해 최소 비용(여기서는 -를 사용해 최대 비용의 간선)을 추출
graph = []
for _ in range(w):
    s, e, w = map(int, input().strip().split())
    # 파이썬의 기본 heapq는 최소힙이기 때문에 마이너스를 붙여 최대힙으로 바꿔줌
    # 힙에 대해 더 공부해야 할 필요가 있다...
    # 비용이 최대인 것부터 순서대로 graph 앞에 둠
    heapq.heappush(graph, (-w, s, e))

answer = 0

# 그래프에서 최소 비용의 간선을 하나씩 추출하면서, 각 노드가 같은 집합에 속해 있지 않으면
# 두 노드를 연결하고, 비용 누적
while graph:
    w, s, e = heapq.heappop(graph)
    w = -w
    union_parent(parent, s, e)
    # 최종 연결된 노드가 c와 v인 경우, 종료
    if find_parent(parent, c) == find_parent(parent, v):
        answer = w
        break
print(answer)


