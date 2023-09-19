# 외판원 순회2
'''
N : 도시의 수
W : 비용
순열
'''
import sys

def backtracking(cnt, now, total):
    global min_total

    if total >= min_total:
        return

    # 길이가 N이 되면 최솟값 비교
    if cnt == N:
        # 돌아가는 비용
        if W[now][i]:
            total += W[now][i]
            if total < min_total:
                min_total = total

    # 반복문
    for w in range(N):
        if visited[w] == 0 and W[now][w]:
            # 들어가기 전 로직 - 경로 저장 & total 계산
            visited[w] = 1
            total += W[now][w]
            # 다음 재귀 호출
            backtracking(cnt + 1, w, total)
            # 로직 후 초기화
            visited[w] = 0
            total -= W[now][w]


N = int(sys.stdin.readline())

W = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]

arr = [i for i in range(N)]

min_total = 99999999

for i in range(N):
    visited = [0] * N
    visited[i] = 1
    backtracking(1, i, 0)


print(min_total)