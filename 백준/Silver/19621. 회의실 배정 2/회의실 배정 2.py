# 19621 회의실 배정2
# 각 회의마다 인원이 다르고 앞과 뒤의 회의랑 회의시간이 무조건 겹치기 때문에
# 브루트포스 방법
import sys

input = sys.stdin.readline
N = int(input().strip())

def dfs(n, val):
    global res
    # 만약 n이 N보다 크거나 같고, 최종 결과값이 당시의 회의 참석 인원수보다 작다면
    if n >= N and res < val:
        # 값을 덮어씌우고
        res = val
        # return
        return

    # 모든 경우에 대해서 계산
    for i in range(n, N):
        dfs(i+2, val+arr[i][2])

arr = [list(map(int, input().strip().split())) for _ in range(N)]
arr.sort()
# res : 결과값
res = 0
# 0부터 시작. val = 당시의 회의 참석 인원 수
dfs(0, 0)
print(res)