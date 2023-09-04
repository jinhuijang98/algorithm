import sys
input = sys.stdin.readline

def bfs(s):
    q = []
    q.append(s)         # 시작점 q에 append
    visited = [0] * n       # 1차원 배열 만들기
    # visited[s] = 1
    while q:
        x = q.pop(0)    # 시작점
        for i in range(n):
            if x != i and arr[x][i] == "Y" and visited[i] == 0:
                visited[i] = visited[x] + 1     # 방문한적 없고 친구라면 그리고 본인이 아니라면 +1씩
                # x = i
                q.append(i)     # append
    cnt = 0
    for j in range(n):
        if j!=s and visited[j] >= 1 and visited[j] < 3:     # 본인 자신이 아니면서 방문이 1보다 크고 3보다 작다면 친구의 친구까지
            cnt += 1
    return cnt
# n : 사람의 수
n = int(input().strip())

# 친구 배열
arr = [list(input().strip()) for _ in range(n)]


max_v = 0
for k in range(n):
    friend = bfs(k)
    if max_v < friend:
        max_v = friend
print(max_v)
