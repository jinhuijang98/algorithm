# https://www.acmicpc.net/problem/1389

# 1389 케빈 베이컨의 6단계 법칙
'''
최대 6단계 이내 서로 아는 사람으로 연결
케빈 베이컨 게임 : 임의의 두 사람이 최소 몇 단계 만에 이어질 수 있는지 계산
Baekjoon Online Judge의 유저 중에서 케빈 베이컨의 수가 가장 작은 사람 찾기
케빈 베이컨 수는 모든 사람과 케빈 베이컨 게임을 했을 때 나오는 단계의 합
'''

import sys
input = sys.stdin.readline

n, m = map(int, input().strip().split())

# 인접 리스트
adj_list = [[] for _ in range(n+1)]
# print(adj_list)

for _ in range(m):
    a, b = map(int, input().strip().split())
    adj_list[a].append(b)
    adj_list[b].append(a)


def bfs(s):
    q = []
    q.append(s)
    visited = [0] * (n + 1)
    visited[s] = 1
    while q:
        x = q.pop(0)
        for i in adj_list[x]:
            if visited[i] == 0:
                q.append(i)
                visited[i] = visited[x] + 1
    bacon = 0
    for i in range(1, n+1):
        bacon += visited[i] - 1
    return bacon

min_val = 100000000000000000000000
for i in range(1, n+1):
    if min_val > bfs(i):
        min_val = bfs(i)
        result = i
print(result)




