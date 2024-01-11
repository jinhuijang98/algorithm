import sys
from collections import deque
input = sys.stdin.readline
# n : 정점의 개수
# m : 간선의 개수
# v : 탐색을 시작할 정적의 번호
n, m, v = map(int, input().strip().split())

'''
양방향
단, 방문할 수 있는 정점이 여러 개인 경우에는 정점 번호가 작은 것을 먼저 방문하고
더 이상 방문할 수 있는 점이 없는 경우 종료한다. 정점 번호는 1번부터 N번
'''

def dfs(v):
    visited1[v] = True
    print(v, end=" ")
    for i in graph[v]:
        if not visited1[i]:
            dfs(i)


def bfs(v):
    q = deque()
    q.append(v)
    visited2[v] = True
    while q:
        now = q.popleft()
        print(now, end=" ")
        # 인접했으면서
        for i in graph[now]:
            # 아직 방문하지 않았다면
            if not visited2[i]:
                visited2[i] = True
                q.append(i)

graph = [[] for _ in range(n+1)]
for i in range(m):
    s, t = map(int, input().strip().split())
    graph[s].append(t)
    graph[t].append(s)

# dfs의 방문 기록
visited1 = [False] * (n+1)

# bfs의 방문 기록
visited2 = [False] * (n+1)
# 정렬
for i in graph:
    i.sort()
dfs(v)
print()
bfs(v)