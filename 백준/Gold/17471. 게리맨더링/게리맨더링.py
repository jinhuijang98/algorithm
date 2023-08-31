import sys
input = sys.stdin.readline

'''
1. 부분 집합으로 나눔
2. 연결되어 있는지 확인
3. 연결되어 있다면 차이가 최소가 되도록
'''
def dfs(s, group):
    stack = []
    visited = [0] * (n+1)
    visited[s] = 1
    if len(group) == 1:
        return 1
    else:
        while True:
            # 인접해있고, 방문한적 없다면 + 그룹 내의 값만 확인
            for i in adj[s]:
                if visited[i] == 0 and i in group:
                    stack.append(i)
                    s = i
                    visited[s] = 1
            else:
                if stack:
                    s = stack.pop()
                else:
                    break
        cnt = 0
        for i in group:
            if visited[i] != 0:
                cnt += 1
        if cnt == len(group):
            # print(visited)
            return 1
        else:
            # print(visited)
            return 0

# n : 구역의 개수
n = int(input().strip())
# 구역의 개수에 따른 1~n개 구역 리스트로 만들기
n_list = [i for i in range(1, n+1)]
# num_peo : 각 구역의 인구
num_peo = list(map(int, input().strip().split()))
# 인접 정보
adj = [[] for _ in range(n+1)]
for i in range(n):
    xx = list(map(int, input().strip().split()))
    adj[i+1] = xx[1:]

# 구역의 개수에 따라 부분집합 만들기
result = False
min_v = 1000000
for i in range(1, 1<<(n-1)):
    group1 = []
    group2 = []
    total1 = 0      # group1의 인구수
    total2 = 0      # group2의 인구수
    for j in range(n):      # 부분집합 만들기
        if i&(1<<j):
            group1.append(n_list[j])
            total1 += num_peo[n_list[j]-1]
        else:
            group2.append(n_list[j])
            total2 += num_peo[n_list[j]-1]

    # 인접 여부 확인 => dfs로
    one_check = dfs(group1[0], group1)
    two_check = dfs(group2[0], group2)

    # 만약 group1과 group2모두가 dfs로 연결되어 있음이 확인된다면
    if one_check==1 and two_check == 1:
        result = True
        # 최소값 갱신
        if min_v > abs(total1 - total2):
            min_v = abs(total1 - total2)

# 최소값이 갱신된 적 없다면 = 구역을 나눌 수 없다면 (result는 false)
if result is False:
    print(-1)   # -1 출력
else:       # 최소값이 한번이라도 갱신된 적 있다면 = 구역을 나누는 경우의 수가 존재하므로
    print(min_v)   # 결과값 출력
