import sys
input = sys.stdin.readline
# N : 주차 공간의 수, M : 차량의 수
N, M = map(int, input().split())

# 주차공간 s의 단위 무게당 요금 Rs
arr_s = [int(input().strip()) for _ in range(N)]

# 차량들의 무게를 나타내는 정수
# 1부터 M번의
arr_m = [int(input().strip()) for _ in range(M)]

# 주차장 출입순서를 나타내는 정수
arr = [int(input().strip()) for _ in range(2*M)]

# 최종 결과값
rlt = 0
# 방문 확인 리스트
visited = [0]*(N)
# 대기 목록
queue = []
while arr:
    if arr[0] > 0:
        x = arr.pop(0)
        for j in range(N):
            if visited[j] == 0:
                visited[j] = x
                rlt += arr_m[x-1] * arr_s[j]
                break
        else:    # 더 이상 넣을 주차공간이 없을 경우 우선 queue 쌓아둠
            queue.append(x)
    else:
        # arr[0]이 음수일 경우
        x = arr.pop(0)
        for j in range(N):
            if visited[j] == -x:
                visited[j] = 0 # 공간을 다시 비우고
                while queue:    # queue에 남아 있는 거 처리
                    y = queue.pop(0)
                    visited[j] = y
                    rlt += arr_m[y-1] * arr_s[j]
                    break
print(rlt)
