import sys
N, M = map(int, input().split())

heavy_list = [[] for _ in range(N+1)]  # heavy_list[노드] = [노드보다 무거운 것들]
light_list = [[] for _ in range(N+1)]  # light_list[노드] = [노드보다 가벼운 것들]

for _ in range(M):
    heavy, light = map(int, sys.stdin.readline().split())
    heavy_list[heavy].append(light)
    light_list[light].append(heavy)


def DFS(list, root):
    """root보다 가볍거나/무거운 것의 개수 구하는 함수"""
    count = 0
    for node in list[root]:
        if not visited[node]:  # 방문하지 않았으면
            visited[node] = True  # 방문 처리
            count += 1
            count += DFS(list, node)
    return count


mid = (N+1)/2
result = 0

for root in range(1, N+1):
    visited = [False] * (N+1)
    if DFS(heavy_list, root) >= mid:
        result += 1
    if DFS(light_list, root) >= mid:
        result += 1

print(result)