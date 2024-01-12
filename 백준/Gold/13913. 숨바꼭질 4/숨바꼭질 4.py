# 13913 숨바꼭질4

import sys
from collections import deque
input = sys.stdin.readline

'''
수빈이는 동생과 숨바꼭질을 하고 있음
수빈이는 현재 점 N
동생은 점 K
수빈이가 걷는다면 x-1 or x+1
수빈이가 순간이동을 한다면 2*x
수빈이가 동생을 찾을 수 있는 가장 빠른 시간이 몇 초 후인지 ?
처음에는 bfs를 돌리고 그 결과값을 모두 저장해서 경로를 출력한다고 생각했는데 -> 인덱스에러와 시간초과
'''

n, k = map(int, input().strip().split())

# bfs로 확인
'''
만약 k가 n보다 작다면 무조건 x-1씩 움직여야 함 -> 아님

'''

# result = []
# 수빈이가 특정 위치를 방문할 때 걸리는 시간(초)를 나타내는 정보
visited = [0] * 100001
# 자식 노드가 부모 노드를 알기 위한 정보
check = [0] * 100001  # 수빈이가 동생을 만나기 전에 어떤 좌표를 이동했는지 표시하는 정보

# 동생이 있는 위치에 도달하기까지 수빈이가 어떻게 이동을 했는지 확인
def move(now):
    # 경로 탐색 시작
    data = []
    # 역으로 경로 찾기
    temp = now
    # 수빈이가 동생을 만날 때까지의 걸리는 시간만큼 반복하면서
    for _ in range(visited[now]+1):
        # 현재 위치 추가
        data.append(temp)
        # 전의 위치 받기
        temp = check[temp]
    # 거꾸로 출력
    # print(' '.join(map(str, data[::-1])))
    print(*data[::-1])


def bfs():
    q = deque()
    # 수빈이의 시작 위치 받기
    q.append(n)
    while q:
        now = q.popleft()
        # 수빈이가 동생을 만났다면
        if now == k:
            # 걸린 시간 출력
            print(visited[now])
            # 어떻게 움직였는지 출력
            move(now)
            return
        # 수빈이가 이동할 수 있는 3가지 방향(뒤, 앞, 순간이동)을 차례대로 받아
        for next in (now-1, now+1, now*2):
            # 다음 이동할 위치가 이동가능한 좌표이며, 아직 방문하지 않았다면
            if 0 <= next < 100001 and visited[next] == 0:
                # 이동할 위치에 시간 표시
                visited[next] = visited[now] + 1
                # 큐에 이동할 위치를 추가
                q.append(next)
                # 수빈이가 지나온 위치를 알기 위해 다음 이동 위치에 현재 이동위치를 기록
                check[next] = now

bfs()



# 시작점

#
# # cnt = 0
# while q:
#     cnt, now = q.popleft()
#     # 찾았다면 => 기록들을 어떻게 알지? result에 어떻게 담지?
#     if now == k:
#         break
#
#     for i in range(3):
#         if i == 0 :
#             nx = now * 2
#             if  nx <= 100000:
#                 if visited[nx] == 0 and nx <= 100000:
#                     visited[nx] = visited[now] + 1
#                     # cnt1 = cnt
#                     # cnt1 += 1
#                     q.append((visited[nx], nx))
#                     # visited[nx] = 1
#                     result.append([visited[nx], now, nx])
#                     if nx == k:
#                         break
#         elif i == 1:
#             nx = now + 1
#             if nx <= 100000:
#                 if visited[nx] == 0  and nx <= 100000:
#                     visited[nx] = visited[now] + 1
#                     # cnt2 = cnt
#                     # cnt2 += 1
#                     q.append((visited[nx], nx))
#                     # visited[nx] = 1
#                     result.append([visited[nx], now, nx])
#                     if nx == k:
#                         break
#         else:
#             nx = now -1
#             if nx <= 100000:
#                 if visited[nx] == 0 and nx <= 100000:
#                     visited[nx] = visited[now] + 1
#                     # cnt2 = cnt
#                     # cnt2 += 1
#                     q.append((visited[nx], nx))
#                     # visited[nx] = 1
#                     result.append([visited[nx], now, nx])
#                     # cnt3 = cnt
#                     # cnt3 += 1
#                     # q.append((cnt3, nx))
#                     # visited[nx] = 1
#                     # result.append((cnt3, now, nx))
#                     if nx == k:
#                         break
# if cnt > 0:
#     print(cnt-1)
#     path = [[1, 0, n]]
#     # # while True:
#     # xx = result[2].index(k)
#     # while True:
#     # print(result[len(result)-1][2])
#     # print(result)
#     num = k
#     while num != n:
#         for i in range(len(result)):
#             if result[i][2] == num:
#                 num = result[i][1]
#                 path.append(result[i])
#                 break
#     path.sort()
#     for j in range(cnt):
#         print(path[j][2], end=" ")
# else:
#     print(0)
#     print(n)
# #     leng = len(result)
# #     if leng > 0:
# #         for i in range(leng):
# #             if result[i][2] == num:
# #                 # next가
# #                 xx = i
# #                 if xx > 0:
# #                     result = result[:xx+1]
# #                     fin.append(result[xx])
# #                     num = result[xx][1]
# #                     # i = reuslt2[xx][1]
# #                     break
# #                 else:
# #                     # fin.append(result[xx])
# #                     # num = result[xx][1]
# #                     # # i = reuslt2[xx][1]
# #                     break
# #
# #     if num == n or leng==0:
# #         break
# # fin.sort()
# # print(n, end=" ")
# # for i in range(len(fin)):
# #     print(fin[i][2], end=" ")
